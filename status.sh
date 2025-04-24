#/bin/bash
#
# loop printing proc temp, freq and throttled status
#
# 0x50000 means throttling occurred, under-voltage occurred
# 0x50005 means throttled now, under-voltage now
#
while true; do echo -n `date +"%A %D"`; uptime; vcgencmd measure_temp && vcgencmd measure_clock arm && vcgencmd get_throttled; \
  echo -e "vout:\c " && lifepo4wered-cli get vout; echo -e "vin:\c" && lifepo4wered-cli get vin; echo -e "vbat:\c" && lifepo4wered-cli get vbat ; \
  sleep 30; echo ' '; done
