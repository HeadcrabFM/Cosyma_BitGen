@echo off
REM Set code page to UTF-8
chcp 65001 >nul

echo 				* * * * * * * *
echo 				*             *
echo 				* COSYMA Ltd. *
echo 				*             *
echo 				* * * * * * * *
echo 					 2024
echo .
echo .
echo .
echo Сейчас будет произведено ОБНОВЛЕНИЕ
echo УДАЛЁННОГО РЕПОЗИТОРИЯ НА ГИТХАБЕ.
echo (интеграция результатов работы в локальной папке
echo в систему контроля версий в облаке).
echo ------------------------------------------------------------------------
echo Пожалуйста, следуйте указаниям на экране и читайте вывод консоли.
echo Успешность обновления Гитхаба можно проверить в браузере.
echo Если что-то сломалось, обратитесь в админу:
echo ------------------------------------------------------------------------
echo 		gs@cosyma.pro			+79217916237				    
echo ------------------------------------------------------------------------

:: Запрос комментария для коммита
set /p comment="Комментарий:      "

echo ------------------------------------------------------------------------

:: Добавление всех изменений в индекс
git add .

:: Коммит с пользовательским сообщением
git commit -m "%comment%"

:: Пуш изменений в ветку 'master' на удаленный репозиторий 'origin'
git push -u origin master

echo ------------------------------------------------------------------------

:: Подтверждение завершения
echo Скрипт завершил работу, файлы загружены в систему контроля версий.
echo пожалуйста, проверьте успешность через браузер, в случае неудачи
echo следуйте указаниям в консоли выше, либо обратитесь к админу

endlocal
pause