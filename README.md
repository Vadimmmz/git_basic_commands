## Useful websites
- [https://learngitbranching.js.org/](https://learngitbranching.js.org/)

## **Git commands**
```bash 
git init
git status
echo "venv" > .gitigore
echo "Message1\nTestmessage2" >> .gitignore

# To add all files in git
git add .

    
echo "Message1\nTestmessage2" >> .gitignore
git commit -m "Initial commit"  
git log
git push

git remote add origin 'httpadress.git'
git push --set-upstream origin main


# Make a new branch / создание ветки 
git branch fix-me

# Branch deleting / удаление ветки
git branch -D fix-me 

# view all branches / просмотр всех веток
git branch

# switching to adifferent branch / переключение на новую ветку
got switch fix-me
git checkout fix-me 

# seeing difference between files that consist in different branches
git diff

# To get all remote branches for local using
git fetch

# For creating new banch and checkout on it
git checkout -b calc
git switch -c calc

# To get changes from remote server
git pull

# For connect to remote branch
git ls-remote
git checkout origin/laptop_branch

# For restore the working tree files with the content from the given tree 
git restore .
git restore <filename>

# Show settings
git config --list

# Show name of current user
git config --show-origin --get user.name

# To watch history of commits
git log

# to see difference between HEAD and the current file state or a definite commit
git diff <filename>
git diff <commit id>
```




