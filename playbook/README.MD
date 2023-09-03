# Плейбук к тестовому заданию на буткамп.

## Задание:

```
Необходимо написать Ansible playbook, который выполняет на хосте следующие действия:

    создает нового пользователя cloudru с паролем cloudpass
    разрешает на хосте авторизацию через ssh по ключу
    запрещает логин по ssh от пользователя root
    копирует предоставленный публичный ключ для пользователя cloudpass
```

## Запуск

### Установка

```
git clone https://github.com/iGenerick/devops_camp.git

cd devops_camp/playbook
```

### Запуск

Возможно несколько варианта запуска плейбука.
один из них - указание переменных непосредственно при запуске:

```$ ansible-playbook -i hosts playbook.yml -e "hosts_group=testservers testserver_user=user testserver_password=password new_user=cloudru new_pass=cloudpass" --ssh-extra-args='-o StrictHostKeyChecking=no'```

$ второй с использованием ansible-vault

```ansible-playbook -e @vault --ask-vault-pass -i hosts playbook.yml --ssh-extra-args='-o StrictHostKeyChecking=no'```

в "боевом" окружении лучше предварительно получить ssh fingerprint целевых хоста(-ов), тогда опцию ```--ssh-extra-args='-o StrictHostKeyChecking=no'```  можно будет не указывать и настроить ssh-key для работы ansible (ключи можно указать при развертывании системы).