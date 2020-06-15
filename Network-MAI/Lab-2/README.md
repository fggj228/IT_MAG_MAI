# Лабораторная работа 2
### Подготовка

![status](Im/vagr_status.png)

### Настройка роутера 1
```
sudo vtysh                    # вход в quagga
configure terminal            # вход режим глобальной конфигурации
router ospf                   # вход в режим настройки роутера
router-id  10.0.0.1           # присвоение id роутеру
passive-interface default     # выключение машрута по умолчанию
network 172.16.0.0/24 area 0  # присвоение area 0 сети 172.16.0.0/24
no passive-interface eth1     # включение интерфеса eth1
default-information originate # включение распространения маршрута по умолчанию
exit                          # выход в глобальной конфигурации
exit                          # выход в основной режим
copy running-config startup-config # сохранение новой конфигурации
exit                          # выход в консоль
sudo iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE  # включение маскарада на интерфейсе eth1
```
![r1](Im/r1.png)

### Настройка роутера 2
```
sudo vtysh                    # вход в quagga
configure terminal            # вход режим глобальной конфигурации
router ospf                   # вход в режим настройки роутера
router-id  10.0.0.2           # присвоение id роутеру
passive-interface default     # выключение машрута по умолчанию
no passive-interface eth1     # включение интерфеса eth1
network 172.16.0.0/24 area 0  # присвоение area 0 сети 172.16.0.0/24
no passive-interface eth2     # включение интерфеса eth2
network 172.16.1.0/24 area 1  # присвоение area 1 сети 172.16.1.0/24
no passive-interface eth3     # включение интерфеса eth3
network 172.31.0.0/24 area 0  # присвоение area 0 сети 172.31.0.0/24
exit                          # выход в глобальной конфигурации
exit                          # выход в основной режим
copy running-config startup-config # сохранение новой конфигурации
```
![r2](Im/r2.png)

### Настройка роутера 3
```
sudo vtysh                     # вход в quagga
configure terminal             # вход режим глобальной конфигурации
router ospf                    # вход в режим настройки роутера
router-id  10.0.0.3            # присвоение id роутеру
passive-interface default      # выключение машрута по умолчанию
no passive-interface eth1      # включение интерфеса eth1
network 172.16.0.0/24 area 0   # присвоение area 0 сети 172.16.0.0/24
no passive-interface eth2      # включение интерфеса eth2
network 192.168.0.0/24 area 0  # присвоение area 1 сети 192.168.0.0/24
no passive-interface eth3      # включение интерфеса eth3
network 172.31.0.0/24 area 0   # присвоение area 0 сети 172.31.0.0/24
exit                           # выход в глобальной конфигурации
exit                           # выход в основной режим
copy running-config startup-config # сохранение новой конфигурации
```
![r3](Im/r3.png)

### Настройка роутера 4
```
sudo vtysh                              # вход в quagga
configure terminal                 # вход режим глобальной конфигурации
router ospf                        # вход в режим настройки роутера
router-id  10.0.0.4                # присвоение id роутеру
passive-interface default          # выключение машрута по умолчанию
no passive-interface eth1          # включение интерфеса eth1
network 172.16.1.0/24 area 1       # присвоение area 0 сети 172.16.1.0/24
no passive-interface eth2          # включение интерфеса eth2
network 192.168.1.0/24 area 1      # присвоение area 1 сети 192.168.1.0/24
exit                               # выход в глобальной конфигурации
exit                               # выход в основной режим
copy running-config startup-config # сохранение новой конфигурации
```
![r4](Im/r4.png)