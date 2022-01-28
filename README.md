# 1.介绍

**C++使用查表法实现的由公历日期查询以下几个内容**

1. 农历日期
2. 年干支-月干支-日干支-时干支
3. 节气（精确到秒）

# 2.查询范围

以下范围内，程序有效。

**开始日期：1900年01月31日（含）起有效。**

**结束日期：2098年12月31日（含）结束有效。**

**注意：本程序的四干支以 《立春》 作为新的一年的起始为标准。**

以上的日期范围内，与[寿星天文历](http://www.nongli.net/sxwnl/)数据完全一致，包括节气的具体时间与寿星万年历分秒不差（寿星万年历使用的是天文算法计算出来的时间，但是本程序仅在上诉范围日期内使用，故为了简化，本程序的实现是通过查表的原理）。

# 3.文件结构

两个文件，一个头文件，一个CPP文件，接口都封装在里面。

```shell
calendar.h  # 10 KB
calendar.cpp # 143 KB
```

部分头文件内容：

```c++
class Calendar
{
    /*
     * ************************************************************************************************
     * ************************************************************************************************
     * **********                                                                           
     * **********   1.【功能】根据公历日期查 农历日期、四干支、节气（精确到秒）                    
     * **********                                                                          
     * **********   2.【重要信息】本程序的干支是以 <立春> 为界限（精确到秒）                     
     * **********                                                                           
     * **********   3.【支持的时间段】公历 1900-01-31 至 2098-12-31                            
     * **********   此时间段内时间标准与 寿星天文历[http://www.nongli.net/sxwnl/]数据完全一致    
     * **********                                                                          
     * **********   4.【实现】 因使用跨度和信息很少，因此使用查表法实现                         
     * **********                                                                          
     * **********                                                                  -- by taynpg     
     * *************************************************************************************************
     * *************************************************************************************************
    */
    /*
     * 《使用方法》
     *  新建一个 Calendar 对象后
     *  先调用以下函数进行 公历 [年月日时分秒]录入，即可使用其他内容。
     *  bool SetSolarDate(int year, int month, int day, int hour, int min = 0, int second = 0);
    */
    /* 本程序的初始化入口函数 */
public:
    // 录入公历日期（同一个对象可以反复调用），如果日期不合法，返回 false
    // 最后两个参数 分钟 秒钟 默认为 0，可以不填写（若传入的日期当天有节气，则可能会对结果有影响）。
    // (若传入的日期当天没有节气，则对结果无影响、因此若日期当日有节气信息，建议传入精确时间)。
    bool SetSolarDate(int year, int month, int day, int hour, int min = 0, int second = 0);

    /* 该部分是传入的内容 (用户主要使用的部分) */
public:
    int solarYear = 0;          // 公历年 4 位数字
    int solarMonth = 0;         // 公历月
    int solarDay = 0;           // 公历日
    int solarHour = 0;          // 公历小时
    int solarMin = 0;           // 公历分
    int solarSecond = 0;        // 公历秒

/* 该部分是计算出来的内容 (用户主要使用的部分) */
public:
    int lunarYear = 0;           // 农历年 4 位数字
    int lunarMonth = 0;          // 农历月
    int lunarDay = 0;            // 农历日
    bool isBigMonth = false;     // 农历的月 月大还是月小，(月大 30 天，月小 29 天)。
    bool isLeapMonth = false;    // 当前农历月是否为农历闰月

    std::string lunarYearZhu = "";    // 年干支信息(两个字)，如 甲子
    std::string lunarMonthZhu = "";   // 月干支信息(两个字)，如 甲子
    std::string lunarDayZhu = "";     // 日干支信息(两个字)，如 甲子
    std::string lunarHourZhu = "";    // 时干支信息(两个字)，如 甲子
    std::string jieQiOne = "";        // 本月第一个节气信息，返回格式示例 （04-04-清明-时间13:12:44）
    std::string jieQiTwo = "";        // 本月第二个节气信息，返回格式示例 （04-19-谷雨-时间20:01:14）
```

# 示例代码

```c++
#include "calendar.h"
#include <iostream>

int main()
{
    Calendar* m_calendar = new Calendar;

    if (m_calendar->SetSolarDate(2021, 11, 29, 20, 01, 10))
    {
        std::cout << "农历年:" << m_calendar->lunarYear << std::endl;
        std::cout << "农历月:" << m_calendar->lunarMonth << std::endl;
        std::cout << "农历日:" << m_calendar->lunarDay << std::endl;
        std::cout << "年干支:" << m_calendar->lunarYearZhu << std::endl;
        std::cout << "月干支:" << m_calendar->lunarMonthZhu << std::endl;
        std::cout << "日干支:" << m_calendar->lunarDayZhu << std::endl;
        std::cout << "时干支:" << m_calendar->lunarHourZhu << std::endl;
        std::cout << "当月节气一:" << m_calendar->jieQiOne << std::endl;
        std::cout << "当月节气二:" << m_calendar->jieQiTwo << std::endl;
    }

    delete m_calendar;
    m_calendar = nullptr;

    return 0;
}
```

执行结果：

```shell
# 公历 2021年11月29日  20时01分10秒
```

```shell
农历年:2021
农历月:10
农历日:25
年干支:辛丑
月干支:己亥
日干支:辛巳
时干支:戊戌
当月节气一:11-07-立冬-时间-12:58:37
当月节气二:11-22-小雪-时间-10:33:34
```

# 代码声明

功能不算很多，比较简洁，两个文件一共 153 KB，但已达到我的需求。
