local mp=require("mp")

-- 0:auto‑safe原始多声道  1:auto  2:stereo立体声  3:mono单声道  4:5.1  5:7.1
local function get_mono_state()
    return mp.get_property_number("user-data/mono_toggle", 0)
end

local function set_mono_state(state)
    mp.set_property_number("user-data/mono_toggle", state)
end

local function toggle_mono()
    local curr = get_mono_state()
    local new = (curr + 1) % 6
    set_mono_state(new)

    local msg
    if new == 0 then
        mp.set_property("audio-channels", "auto-safe")
        msg = "🔊 auto‑safe 原始多声道(最佳)"
    elseif new == 1 then
        mp.set_property("audio-channels", "auto")
        msg = "🔊 auto 完全自动"
    elseif new == 2 then
        mp.set_property("audio-channels", "stereo")
        msg = "🔊 立体声已开启"
    elseif new == 3 then
        mp.set_property("audio-channels", "mono")
        msg = "🔊 单声道已开启"
    elseif new == 4 then
        mp.set_property("audio-channels", "5.1")
        msg = "🔊 5.1声道已开启"
    elseif new == 5 then
        mp.set_property("audio-channels", "7.1")
        msg = "🔊 7.1声道已开启"
    end
    -- 居中提示，和你其它脚本统一样式
    mp.set_osd_ass(0,0,"{\\an5\\fs20\\bord2}"..msg)
    mp.add_timeout(1.2,function() mp.set_osd_ass(0,0,"") end)
end

toggle_mono()