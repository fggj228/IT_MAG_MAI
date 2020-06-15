# Лабораторная работа 1
## задание 1
### разобрать структуру нарисовать схему сети
![scheme](Im/scheme.png)

Сети: 
- 192.168.0.0 -- central
- 192.168.1.0 -- ofiice2
- 192.168.2.0 -- office1

## задание 2

### Первая сеть
Подсети:

#### 192.168.2.0/26
Узлов: 62
Broadcast: 192.168.2.63

#### 192.168.2.64/26
Узлов: 62
Broadcast: 192.168.2.127

#### 192.168.2.128/26
Узлов: 62
Broadcast: 192.168.2.191

### Вторая сеть
Подсети:

#### 192.168.1.0/25
Узлов: 126
Broadcast: 192.168.1.127

#### 192.168.1.128/26
Узлов: 62
Broadcast: 192.168.1.191

#### 192.168.1.192/26
Узлов: 62
Broadcast: 192.168.1.255

### Третья сеть
Подсети:

#### 192.168.0.0/28
Узлов: 14
Broadcast: 192.168.0.15

## задание 3

### centralServer

![centralServer](Im/centralServer.png)

### office1Server

![office1Server](Im/office1Server.png)

### office2Server

![office2Server](Im/office2Server.png)



## Задание 4
### Nginx

![nginx](Im/nginx_on_office2Server.png)
![F_ports](Im/Forward_ports.png)

###  Блокировка запроса на 80 порт и ping
![80port](Im/Block_port.png)
![ping](Im/Block_ping.png)
