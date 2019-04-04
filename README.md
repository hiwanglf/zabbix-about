# zabbix-about

## dingtalk alert

### Media-types Configuration
![image](https://github.com/hiwanglf/zabbix-about/blob/master/alertscripts/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190404165356.png?raw=true)

### Action Configuration 
下面只是消息体，操作步骤自己来就行了

```
# Operations

## ATTENTION
<font color=#FF0000>**Severity**: {TRIGGER.SEVERITY} </font>

**HostName**:  {HOST.NAME}

**HostIP**:  {HOST.IP}

**AlertName**:  {TRIGGER.NAME}

**Status**:  {TRIGGER.STATUS}

**Time**:  {EVENT.DATE} {EVENT.TIME}

**EventID**:  {EVENT.ID}

## Detail
**{ITEM.NAME}**: <font color=#FF0000> {ITEM.VALUE} </font>

# Recovery Operations

## RECOVERED
<font color=#0000FF>**Severity**: {TRIGGER.SEVERITY}</font>

**HostName**:  {HOST.NAME}

**HostIP**:  {HOST.IP}

**AlertName**:  {TRIGGER.NAME}

**Status**:  {TRIGGER.STATUS}

**Time**:  {EVENT.DATE} {EVENT.TIME}

**EventID**:  {EVENT.ID}

## Detail
**{ITEM.NAME}**: <font color=#0000FF> {ITEM.VALUE}</font>
```