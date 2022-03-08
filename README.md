# munin-varnish
## Munin varnish 6 plugin
Using reference https://github.com/munin-monitoring/contrib/tree/master/plugins/varnish

```
cd /etc/munin/plugins/
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_backend_traffic
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_transfer_rates
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_request_rate
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_objects
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_uptime
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_threads
ln -s /usr/share/munin/plugins/varnish6/varnish6_ varnish_expunge
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
