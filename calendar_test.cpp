/*
 * @Author       : Leon Lee
 * @Date         : 2022-03-24 18:24:09
 * @LastEditors  : Leon
 * @LastEditTime : 2022-03-24 18:26:57
 * @Description  : file content
 * @FilePath     : \calendar\calendar_test.cpp
 */
#include "calendar.h"
#include "calendar.cpp"
#include <iostream>

int main()
{
    Calendar *m_calendar = new Calendar;

    if (m_calendar->SetSolarDate(2022, 4, 29, 20, 01, 10))
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
