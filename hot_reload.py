import os
import sys
import time
import importlib
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

class HotReloader:
    def __init__(self, watch_paths=None, ignore_patterns=None):
        self.watch_paths = watch_paths or ['.']
        self.ignore_patterns = ignore_patterns or [
            '.git', '__pycache__', '.pyc', '.log', '.pytest_cache', 
            '.venv', 'venv', 'env', '.env'
        ]
        self.loaded_modules = set()
        self.module_times = {}
        self.observer = None
        self.running = False

    def should_ignore(self, path):
        return any(pattern in str(path) for pattern in self.ignore_patterns)

    def get_module_name_from_path(self, file_path):
        """Convert file path to module name"""
        try:
            # Convert absolute path to relative path
            rel_path = os.path.relpath(file_path, '.')
            
            # Remove .py extension and convert path separators to dots
            if rel_path.endswith('.py'):
                module_name = rel_path[:-3].replace(os.sep, '.')
                return module_name
            return None
        except:
            return None

    def reload_module(self, module_name):
        """Reload a specific module"""
        try:
            if module_name in sys.modules:
                print(f"🔄 Reloading module: {module_name}")
                importlib.reload(sys.modules[module_name])
                return True
            else:
                # Try to import if not already loaded
                try:
                    importlib.import_module(module_name)
                    print(f"📦 Imported new module: {module_name}")
                    return True
                except ImportError:
                    return False
        except Exception as e:
            print(f"❌ Error reloading {module_name}: {e}")
            return False

    def reload_changed_file(self, file_path):
        """Handle file change and reload corresponding module"""
        if self.should_ignore(file_path) or not file_path.endswith('.py'):
            return

        module_name = self.get_module_name_from_path(file_path)
        if module_name:
            self.reload_module(module_name)

class HotReloadHandler(FileSystemEventHandler):
    def __init__(self, reloader):
        self.reloader = reloader

    def on_modified(self, event):
        if not event.is_directory:
            self.reloader.reload_changed_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.reloader.reload_changed_file(event.src_path)

# Global reloader instance
_reloader = None

def start_hot_reload(watch_paths=None, ignore_patterns=None):
    """Start the hot reload system"""
    global _reloader
    
    if _reloader is not None:
        print("🔥 Hot reload is already running!")
        return _reloader
    
    _reloader = HotReloader(watch_paths, ignore_patterns)
    
    # Set up file system observer
    _reloader.observer = Observer()
    handler = HotReloadHandler(_reloader)
    
    for path in _reloader.watch_paths:
        if os.path.exists(path):
            _reloader.observer.schedule(handler, path, recursive=True)
            print(f"👀 Watching: {os.path.abspath(path)}")
    
    _reloader.observer.start()
    _reloader.running = True
    
    print("🔥 Hot reload started! Changes will be automatically applied.")
    print("   Modify any .py file and see changes take effect immediately.")
    
    return _reloader

def stop_hot_reload():
    """Stop the hot reload system"""
    global _reloader
    
    if _reloader and _reloader.observer:
        _reloader.observer.stop()
        _reloader.observer.join()
        _reloader.running = False
        print("🛑 Hot reload stopped.")
        _reloader = None

def reload_module_by_name(module_name):
    """Manually reload a specific module by name"""
    global _reloader
    if _reloader:
        return _reloader.reload_module(module_name)
    else:
        # Create temporary reloader for manual reload
        temp_reloader = HotReloader()
        return temp_reloader.reload_module(module_name)

def is_hot_reload_running():
    """Check if hot reload is currently active"""
    global _reloader
    return _reloader is not None and _reloader.running

# Decorator for auto-reloadable functions
def auto_reload(func):
    """Decorator to make functions auto-reloadable"""
    def wrapper(*args, **kwargs):
        # Get the module of the function
        module = sys.modules[func.__module__]
        module_file = getattr(module, '__file__', None)
        
        if module_file and _reloader:
            # Check if module file was modified
            try:
                current_mtime = os.path.getmtime(module_file)
                last_mtime = _reloader.module_times.get(func.__module__, 0)
                
                if current_mtime > last_mtime:
                    print(f"🔄 Auto-reloading {func.__module__} for {func.__name__}")
                    _reloader.reload_module(func.__module__)
                    _reloader.module_times[func.__module__] = current_mtime
                    
                    # Get the reloaded function
                    reloaded_module = sys.modules[func.__module__]
                    reloaded_func = getattr(reloaded_module, func.__name__)
                    return reloaded_func(*args, **kwargs)
            except:
                pass
        
        return func(*args, **kwargs)
    
    return wrapper
