#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

from prettytable import PrettyTable
c = {
  'header' : '\033[95m',
  'heading' : '\x1b[5;32;40m',
  'blue' : '\033[34m',
  'green' : '\033[32m',
  'red' : '\033[31m',
  'purple' : '\033[35m',
  'cyan' : '\033[36m',
  'yellow' : '\033[33m',
  'warning' : '\033[93m',
  'fail' : '\033[91m',
  'e' : '\033[0m',
  'bold' : '\033[1m',
  'underline' : '\033[4m',
  'red_bg' : '\033[41m',
  'green_bg' : '\033[42m',
  'yellow_bg' : '\033[43m',
  'blue_bg' : '\033[44m',
  'purple_bg' : '\033[45m',
  'cyan_bg' : '\033[46m',
  'white_bg' : '\033[47m',
  'black_bg' : '\033[40m',
}


rpiBplus = {
  'heading' : [ c['heading'] + 'Name Side A', 'PIN Side A', 'PIN Side B', 'Name Side B', 'WiringPi' + c['e'] ],
  'rows' : 
    [
      [c['yellow_bg'] + '3V3 Power' + c['e'], 1, 2, c['red_bg'] + '5V Power' + c['e'], '' ], 
      [c['purple'] + 'GPIO2 SDA1 I2C' + c['e'], 3, 4,  c['red_bg'] + '5V Power' + c['e'], '' ],
      [c['purple'] + 'GPIO3 SCL1 I2C' + c['e'], 5, 6, c['black_bg'] + 'Ground' + c['e'], '' ],
      [c['green'] + 'GPIO4' + c['e'], 7, 8, c['blue'] + 'GPIO14 UART0_TXD' + c['e'], '15' ],
      [c['black_bg'] + 'Ground' + c['e'], 9, 10,  c['blue'] + 'GPIO15 UART0_TXD' + c['e'], '16' ],
      [c['green'] + 'GPIO17' + c['e'], 11, 12, c['green'] + 'GPIO18 PCM_CLK' + c['e'], '1' ],
      [c['green'] + 'GPIO27' +c['e'], 13, 14,  c['black_bg'] + 'Ground' + c['e'], '' ],
      [c['green'] + 'GPIO22' + c['e'], 15, 16, c['green'] + 'GPIO23' + c['e'], '4' ],
      [c['yellow_bg'] + '3V3 Power' + c['e'], 17, 18, c['green'] + 'GPIO24' + c['e'], '5' ],
      [c['blue'] + 'GPIO10 SPIO_MOSI' + c['e'], 19, 20,  c['black_bg'] + 'Ground' + c['e'], '' ],
      [c['blue'] + 'GPIO9 SPIO_MOSI' + c['e'], 21, 22, c['green'] + 'GPIO25' + c['e'], '6' ],
      [c['blue'] + 'GPIO11 SPIO_MOSI' + c['e'], 23, 24, c['blue'] + 'GPIO8 SPIO_CE0_N' + c['e'], '10' ],
      [c['black_bg'] + 'Ground' + c['e'], 25, 26, c['blue'] + 'GPIO7 SPIO_CE1_N' + c['e'], '11' ],
      [c['yellow'] + 'ID_SD 12C ID EEPROM' + c['e'], 27, 28, c['yellow'] + 'ID_SC 12C ID EEPROM' + c['e'], '31' ],
      [c['green'] + 'GPIO5' + c['e'], 29, 30,  c['black_bg'] + 'Ground' + c['e'], '' ],
      [c['green'] + 'GPIO6' + c['e'], 31, 32,  c['green'] + 'GPIO12' + c['e'], '26' ],
      [c['green'] + 'GPIO13' + c['e'], 33, 34,  c['black_bg'] + 'Ground' + c['e'], '' ],
      [c['green'] + 'GPIO19' + c['e'], 35, 36,  c['green'] + 'GPIO16' + c['e'], '27' ],
      [c['green'] + 'GPIO26' + c['e'], 37, 37,  c['green'] + 'GPIO20' + c['e'], '28' ],
      [c['black_bg'] + 'Ground' + c['e'], 39, 40,  c['green'] + 'GPIO21' + c['e'], '29' ],
    ]
}

t = PrettyTable(rpiBplus['heading'])
t.border = True
t.header = True
t.padding_width = 2
t.vertical_char = '|'
t.horizontal_char = '-'
t.junction_char = '*'

print "Pi Model B+"
for row in rpiBplus['rows']:
  t.add_row(row)
print t
