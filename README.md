# ADNI dataset organization
Organize the entire ADNI dataset based on the group name (AD, MCI, CN) locally.

## Prerequisites
- Python 3.9 or later

## How to use
1. Clone the repository to your local machine.
2. Copy the `script.py` to the root directory of the ADNI dataset.
3. Change the csv file name in the `script.py` to the name of the csv file that contains the list of the subjects.
4. Create 3 empty directories in the root directory of the ADNI dataset and name them `AD`, `MCI`, and `CN`.
5. Run the `script.py` using the following command:
```bash
python script.py
```
6. The script will organize the dataset based on the group name (AD, MCI, CN).

## License
This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.