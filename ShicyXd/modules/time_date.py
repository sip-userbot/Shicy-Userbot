# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting the date
    and time of any country or the userbot server.  """

from datetime import datetime as dt

from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, COUNTRY, TZ_NUMBER
from ShicyXd.shicy import shicy_cmd
from Stringchiy import get_string


async def get_tz(con):
    """Get time zone of the given country."""
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")

    for c_code in c_n:
        if con == c_n[c_code]:
            return c_tz[c_code]
    try:
        if c_n[con]:
            return c_tz[con]
    except KeyError:
        return


@shicy_cmd(pattern="time(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def time_func(tdata):
    """For .time command, return the time of
    1. The country passed as an argument,
    2. The default userbot country(set it by using .settime),
    3. The server where the userbot runs.
    """
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)

    t_form = "%H:%M"
    c_name = None

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await tdata.edit(get_string("timdat_1").format(dt.now().strftime(t_form)))
        return

    if not timezones:
        await tdata.edit(get_string("timdat_2"))
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = get_string("timdat_3").format(c_name)

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += get_string("timdat_4")
            return_str += get_string("timdat_5")
            return_str += get_string("timdat_6").format(cmd, c_name)

            await tdata.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(t_form)

    if c_name != COUNTRY:
        await tdata.edit(get_string("timdat_7").format(dtnow, c_name, time_zone)
        )
        return

    if COUNTRY:
        await tdata.edit(get_string("timdat_9").format(dtnow, COUNTRY, time_zone)
        )
        return


@shicy_cmd(pattern="date(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?")
async def date_func(dat):
    """For .date command, return the date of
    1. The country passed as an argument,
    2. The default userbot country(set it by using .settime),
    3. The server where the userbot runs.
    """
    con = dat.pattern_match.group(1).title()
    tz_num = dat.pattern_match.group(2)

    d_form = "%d/%m/%y - %A"
    c_name = ""

    if len(con) > 4:
        try:
            c_name = c_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await dat.edit(get_string("timdat_8").format(dt.now().strftime(d_form))
        )
        return

    if not timezones:
        await dat.edit(get_string("timdat_2"))
        return

    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = get_string("timdat_3").format(c_name)

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += get_string("timdat_4")
            return_str += get_string("timdat_5")
            return_str += get_string("timdat_6").format(cmd, c_name)

            await dat.edit(return_str)
            return

    dtnow = dt.now(tz(time_zone)).strftime(d_form)

    if c_name != COUNTRY:
        await dat.edit(get_string("timdat_9").format(dtnow, c_name, time_zone)
        )
        return

    if COUNTRY:
        await dat.edit(get_string("timdat_9").format(dtnow, COUNTRY, time_zone)
        )
        return


CMD_HELP.update(
    {
        "timedate": f"**Plugin : **`timedate`\
        \n\n  »  **Perintah :** `{cmd}time` <country name/code> <timezone number>\
        \n  »  **Kegunaan : **Dapatkan waktu suatu negara. Jika suatu negara memiliki beberapa zona waktu, itu akan mencantumkan semuanya dan memungkinkan Anda memilihnya.\
        \n\n  »  **Perintah :** `{cmd}date` <country name/code> <timezone number>\
        \n  »  **Kegunaan : **Dapatkan tanggal suatu negara. Jika suatu negara memiliki beberapa zona waktu, itu akan mencantumkan semuanya dan memungkinkan Anda memilihnya.\
    "
    }
)
