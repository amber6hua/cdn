local mp=require("mp")

-- 对比度：单击+5，上限100，超过回到0(原始默认)
local function toggle_contrast()
    local con = mp.get_property_number("contrast", 0)
    con = con + 5
    if con > 100 then
        con = 0
    end
    mp.set_property("contrast", con)
    local msg = string.format("🌑 对比度：%d", con)
    mp.set_osd_ass(0,0,"{\\an5\\fs20\\bord2}"..msg)
    mp.add_timeout(1.2,function() mp.set_osd_ass(0,0,"") end)
end

toggle_contrast()