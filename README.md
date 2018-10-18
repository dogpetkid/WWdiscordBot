# Intro to git

Firstly, [this](http://rogerdudler.github.io/git-guide/) is a useful thing to look at, but I will explain it here. 

What you first need to do is download gitbash from [here](https://git-scm.com/downloads). Choose Windows and then download.

Next install this and then open it.

After you open it, you should be shown a user and directory. From here do `cd ~/Documents` to move to your documents and then `mkdir ./github; cd ./github` to make a github folder and move into it. After this you should make a folder dedicated to this project. To do this, do `mkdir ./WWdiscordBot` or name it whatever you want, just make sure you remember if you named it differently (from here on I will refer to the project folder as `WWdiscordBot`).
After this step is complete you should be able to open you file explore, go to your Documents/github and then see a folder called WWdiscordBot. (If you don't see this, **DON'T continue**, go back and redo those steps.)

Now, back inside of your `WWdiscordBot` (if you need to go back to this folder, do `cd ~/Documents/github/WWdiscordBot`), you will do `git init` which will set up your local repository. The next step is to do `git remote add origin https://github.com/dogpetkid/WWdiscordBot.git` which will point your repository to this one. To make sure this is done right, doing `git remote -v` should say the link above and there should be a neat little blue `(master)` tag next to your directory to show you are on the master branch.

*These next steps have yet to be tested on someone else's computer so if they do not work, this is why.* After being added to the repository, you can then do `git fetch origin` which will get the most recent version of this repository and clone it to your version. After this, you should be set to do work on the repository.

## Basics of git

For the purpose of my example, let's create a file called `yourname.txt` where you change that to be your first name. In this file, simply write your name (full or last, doesn't matter) and save it in the `WWdiscordBot`.

Back inside of your gitbash, you will need to tell git you changed the this file, to do this, we do `git add yourname.txt`. Now we need to do `git commit -m "yourname"`. After this we want to do `git push origin master` to then push this change to the repository (this will be visible to everyone at this point).

# Python

This project will be programmed in python, saying such, you should download [Python 3](https://www.python.org/downloads/release/python-370/) (I will need to find which one is portable and contains pip) and [documentation is here](https://docs.python.org/3/).

For getting the proper module needed for, we must do `cd /c/Users/<student>/AppData/Local/Programs/Python/Python37-32/Scripts/`. *This is if you have python installed, I will need to find where it is otherwise.* *Make sure to change `<student>` with your first intiaial + last name + birth date.* At this point we can now do `./pip3.exe install -U git+https://github.com/Rapptz/discord.py@rewrite` which will give us our discord module we will be using. *I know not of the specifics, but the purpose to the oddly structured command is because the actual discord install is for Python 3.4-3.6 so it is longer to change it to Python 3.7.* *Side note, solution is from [here](https://github.com/Rapptz/discord.py/issues/1637#issuecomment-426805293) if interested.*
