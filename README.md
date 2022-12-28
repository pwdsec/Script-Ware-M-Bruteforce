# Script-Ware-M-Bruteforce
Works only on macOS and it is required to have SWMAuth2

- basic script that can be modified with threading etc
- to get SWMAuth2 just unpact the macos application asar and you will find it there

# Using finder.sh to Unpack an asar File and Run main.py

To use finder.sh and unpack an asar file, follow these steps:

1. Open a terminal window and navigate to the directory where finder.sh is located.

2. Run the finder.sh script with the asar file as an argument. For example:

./finder.sh myasarfile.asar

3. The finder.sh script will unpack the asar file and display the path to SWAuth2. Make a note of this path, as you will need it in the next step.

4. Copy the SWAuth2 file to the same directory as main.py.

5. Run main.py by entering the following command:

python main.py

6. main.py will create a user.txt file and add accounts in the format username:pass.

7. To add your own account list, open the user.txt file in a text editor and add your accounts, one per line, in the format username:pass.

8. Save the user.txt file and run main.py again to process the updated list of accounts.

That's it! You should now be able to use finder.sh to unpack an asar file, find the path of SWAuth2, copy the file, and run main.py to create a user.txt file and add accounts in the format username:pass.
