```
sudo apt-get install tor
vi /etc/tor/torrc
```

수정할 내용 (주석 제거)
```
HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:8000
systemctl tor.service restart
```

```
cat /var/lib/tor/hidden_service/hostname
savgquzyg2i6mjipwh7si7vr3ccapuzedb5mk4hnjlmltesfje3lksid.onion
```
