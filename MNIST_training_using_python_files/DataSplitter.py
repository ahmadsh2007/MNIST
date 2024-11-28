def SplitData(data, train_pct, val_pct, test_pct):
    """
    Splits data into train, validation, and test sets based on given percentages.
    Ensures that the total matches the length of the data by incrementally adjusting the sizes.

    Args:
        data (list or any iterable): The dataset to split.
        train_pct (float): Percentage for the training set (e.g., 0.7).
        val_pct (float): Percentage for the validation set (e.g., 0.2).
        test_pct (float): Percentage for the test set (e.g., 0.1).

    Returns:
        tuple: Sizes for train, validation, and test sets.
    """
    total_length = len(data)
    train_size = int(total_length * train_pct)
    val_size = int(total_length * val_pct)
    test_size = int(total_length * test_pct)

    # Adjust sizes if they don't sum up to total_length
    while train_size + val_size + test_size < total_length:
        if test_size + 1 <= total_length:
            test_size += 1
        elif val_size + 1 <= total_length:
            val_size += 1
        elif train_size + 1 <= total_length:
            train_size += 1

    return train_size, val_size, test_size

def main() -> None:
    # Example usage
    data = list(range(100))  # Example dataset
    train_pct = 0.92
    val_pct = 0.01
    test_pct = 0.07
    
    train_size, val_size, test_size = SplitData(data, train_pct, val_pct, test_pct)
    print(f"Data size: {len(data)}, Train size: {train_size}, Validation size: {val_size}, Test size: {test_size}")

if __name__ == '__main__':
    main()