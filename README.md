**Продвинутое изучение git**

Это первоначальный текст.
Отправлено с window10 на ноутбуке

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
```
