import pandas as pd

def main():
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "London", "Paris"]
    }

    df = pd.DataFrame(data)
    print("DataFrame created successfully:")
    print(df)

    assert len(df) == 3, "DataFrame does not have 3 rows"
    print("Test passed!")

if __name__ == "__main__":
    main()
