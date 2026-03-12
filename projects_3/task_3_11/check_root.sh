#!/bin/bash
check_root() {
  if [[ $EUID -eq 0 ]]; then
   echo "OK"
  else
   echo "Скрипт запущен не от лица суперпользователяю Ошибка."
  fi
}

check_root
