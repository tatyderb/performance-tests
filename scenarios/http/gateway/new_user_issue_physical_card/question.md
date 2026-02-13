Здравствуйте.

Достаточно ли прилагать для этой и дальнейших задач скриншоты:
* `docker stats` 3 штуки (до теста, в середине и ближе к концу)
* htop 2 штуки (до теста и ближе к концу теста)

как вы посоветовали в https://stepik.org/lesson/1775505/step/9?discussion=12748686&reply=12748746&unit=1801059

С настроенными графаной и UI prometheus уже приходится много общаться на работе.
Но настраивать и искать ошибки в них - это была работа девопсов и программистов команды.

Ибо две проблемы
1. cadvisor уходит в постоянный рестарт
2. в графане на дашборде (Import via grafana.com ID: 893) видно только CPU, но не видны другие метрики.

Если достаточно, то дальше можно не читать.
Иначе прошу помочь с настройкой cadvisor и дашборды в графане.

# Cadvisor

При использовании `docker_compose.yaml` получаю непрерывную ошибку:

```
W0213 16:58:18.428393       1 machine_libipmctl.go:64] There are no NVM devices!
W0213 16:58:18.649847       1 manager.go:286] Could not configure a source for OOM detection, disabling OOM events: open /dev/kmsg: no such file or directory
F0213 16:58:18.854837       1 cadvisor.go:167] Failed to start manager: inotify_add_watch /sys/fs/cgroup: permission denied
W0213 16:58:29.152793       1 machine_libipmctl.go:64] There are no NVM devices!
W0213 16:58:29.231039       1 manager.go:286] Could not configure a source for OOM detection, disabling OOM events: open /dev/kmsg: no such file or directory
F0213 16:58:29.331095       1 cadvisor.go:167] Failed to start manager: inotify_add_watch /sys/fs/cgroup: permission denied
W0213 16:58:36.129393       1 machine_libipmctl.go:64] There are no NVM devices!
W0213 16:58:36.218749       1 manager.go:286] Could not configure a source for OOM detection, disabling OOM events: open /dev/kmsg: no such file or directory
F0213 16:58:36.326143       1 cadvisor.go:167] Failed to start manager: inotify_add_watch /sys/fs/cgroup: permission denied
W0213 16:58:45.065610       1 machine_libipmctl.go:64] There are no NVM devices!
W0213 16:58:45.145412       1 manager.go:286] Could not configure a source for OOM detection, disabling OOM events: open /dev/kmsg: no such file or directory
F0213 16:58:45.253560       1 cadvisor.go:167] Failed to start manager: inotify_add_watch /sys/fs/cgroup: permission denied
```
Попытки гуглить и ИИ не привели к решению проблемы. Диагностика изменялась, но постоянный рестарт остается.

Пробовали (по очереди и в комплексе в разных вариантах):

* добавить права на запись `/var/run:/var/run:rw`
* `/var/run/docker.sock:/var/run/docker.sock:rw`
* `/sys/fs/cgroup:/sys/fs/cgroup:rw`
* `/sys/fs/cgroup/cpu,cpuacct:/sys/fs/cgroup/cpuacct,cpu`
* `privileged: true`
* заменить версию с v0.47.0 на latest

## Prometheus

`docker logs prometheus 2>&1 | grep error` ничего не дает, визуальный просмотр логов тоже не находит ничего подозрительного.

Но кроме графика CPU никаких общих графиков Memory, Swap, Network нет. См. grafana.png.

## OC

```
NAME="Fedora Linux"
VERSION="43 (MATE-Compiz)"
RELEASE_TYPE=stable
```