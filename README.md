# Folder Creator

This Python script automates the process of creating a series of folders for organizing course materials, specifically tailored to the needs of a Digital Image Processing course (CSE 4227) at your university. It creates 11 folders, each representing a different chapter in the course.

## Prerequisites

Before running the script, make sure you have Python installed on your computer.

## Usage

1. Clone this repository to your local machine:

```shell
git clone https://github.com/MFReshad//Create-Folder-with-python.git
```

2. Open a terminal or command prompt.

3. Navigate to the directory where you cloned the repository.

4. Modify the folder_path variable in the script to specify the path where you want to create the folders. Change it to your desired path.

5. Run the script using Python:
	 **create_folders.py**
     

6. The script will create 11 folders, each named "Chapter - XX" where XX is the chapter number. If a folder already exists, it will notify you. <br>
**#you can change the folder name you want to set and the number folder you want to create.**
## Example

Suppose you want to organize your Digital Image Processing course materials in the "E:/Cse/4.2/CSE 4227 - Digital Image Processing/Lectures/" directory. You would set the `folder_path` variable like this:

```python
folder_path = "E:/Cse/4.2/CSE 4227 - Digital Image Processing/Lectures/"
```

After running the script, you will see output similar to the following:
```
Folder 'Chapter - 01' created successfully.
Folder 'Chapter - 02' created successfully.
Folder 'Chapter - 03' created successfully.
Folder 'Chapter - 04' created successfully.
Folder 'Chapter - 05' created successfully.
Folder 'Chapter - 06' created successfully.
Folder 'Chapter - 07' created successfully.
Folder 'Chapter - 08' created successfully.
Folder 'Chapter - 09' created successfully.
Folder 'Chapter - 10' created successfully.
Folder 'Chapter - 11' created successfully.
```

Now, you will have the necessary folders to organize your course materials conveniently.




## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

