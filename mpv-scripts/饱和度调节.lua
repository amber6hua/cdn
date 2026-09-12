local mp=require("mp")

-- 饱和度：单击+5，上限100，超过回到0(原始默认)
local function toggle_saturation()
    local sat = mp.get_property_number("saturation", 0)
    sat = sat + 5
    if sat > 100 then
        sat = 0
    end
    mp.set_property("saturation", sat)
    local msg = string.format("🎨 饱和度：%d", sat)
    mp.set_osd_ass(0,0,"{\\an5\\fs20\\bord2}"..msg)
    mp.add_timeout(1.2,function() mp.set_osd_ass(0,0,"") end)
end

toggle_saturation()