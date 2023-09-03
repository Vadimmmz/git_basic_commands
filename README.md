**Git commands**

This text was written instead first test.
Send from window10 on laptop.

```bash 
git init
git status
echo "venv" > .gitigore
echo "Message1\nTestmessage2" >> .gitignore

git add .

    
echo "Message1\nTestmessage2" >> .gitignore
git commit -m "Initial commit"  
git log
git push

git remote add origin 'httpadress.git'
git push --set-upstream origin main


# создание ветки 
git branch fix-me

# удаление ветки
git branch -D fix-me 

# просмотр всех веток
git branch

# переключениена новую ветку
git checkout fix-me 

# seeing difference between files that consist in different branches
git diff

# For creating new banch and checkout on it
git checkout -b calc

# To get changes from remote server
git pull

```
Info from VBOX debian
And some text from Windows
