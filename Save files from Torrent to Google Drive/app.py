from qbittorrent import Client

# Подключение к qBittorrent Web UI
qb = Client("http://127.0.0.1:8080/")

# Введите ваши учетные данные 
qb.login("admin", "123456")  

# Теперь вы можете скачать торрент по ссылке
magnet_link = "magnet:?xt=urn:btih:abb33766b319a89e00e331727a946c33ad3ecdcc"  # Замените "..." на реальную ссылку на торрент

qb.download_from_link(magnet_link)
