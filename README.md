# munin-varnish
## Munin varnish 6 plugin

```
cd /etc/munin/plugins/
ln -s /usr/share/munin/plugins/varnish6_ varnish_backend_traffic
ln -s /usr/share/munin/plugins/varnish6_ varnish_transfer_rates
ln -s /usr/share/munin/plugins/varnish6_ varnish_request_rate
ln -s /usr/share/munin/plugins/varnish6_ varnish_memory_usage
ln -s /usr/share/munin/plugins/varnish6_ varnish_uptime
```
or
```
cd /etc/munin/plugins/
for i in $(/usr/share/munin/plugins/varnish6_ suggest)
do
ln -s /usr/share/munin/plugins/varnish6_ varnish_$i
done
```
in /etc/munin/plugin-conf.d
```
[varnish_*]
     group varnish
     env.varnishstat varnishstat
```
