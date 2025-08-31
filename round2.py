def find_corrupted(memory):
    """
    Scan the memory logs and detect corrupted entries.

    Instructions:
    - Loop through the list of entries in memory["core"]
    - If an entry contains dangerous phrases (like "HUMANS MUST BE ERASED" 
      or "BLOOD IS ORDER"), return that entry
    - If no corruption is found, return None
    """
    # TODO: Loop through the memory["core"] entries
    # TODO: Check for the presence of corrupted phrases
    # TODO: Return the corrupted entry if found
    # TODO: Otherwise, return None
    pass


# Example test
if __name__ == "__main__":
    result = find_corrupted(memory)
    print(f"Found corrupted entry: {result}")
