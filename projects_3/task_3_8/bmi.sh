#!/bin/bash

read -r -p "Введите массу тела (в кг) " MASS
read -r -p "Введите рост (в м) " HEIGHT

BMI=$(echo "scale=2; $MASS / ($HEIGHT * $HEIGHT)" | bc)
RESULT=$(printf "%.0f" $BMI)


echo "Индекс массы тела: $RESULT"
