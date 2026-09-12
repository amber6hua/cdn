-- 仅切换三项HDR参数 单击开/再单击关
local function get_toggle_state()
    local state = mp.get_property_bool("user-data/hdr_three_state", false)
    return state
end

local function set_toggle_state(state)
    mp.set_property_bool("user-data/hdr_three_state", state)
end

-- 开启参数
local hdr_on = {
    ["hdr-compute-peak"] = "no",
    ["target-colorspace-hint"] = "yes",
    ["target-trc"] = "hlg"
}

-- 关闭恢复默认
local hdr_off = {
    ["hdr-compute-peak"] = "auto",
    ["target-colorspace-hint"] = "no",
    ["target-trc"] = "auto"
}

local function toggle_hdr()
    local current = get_toggle_state()
    local new_state = not current
    set_toggle_state(new_state)

    local set = new_state and hdr_on or hdr_off
    for k,v in pairs(set) do
        mp.set_property(k, v)
    end

    if new_state then
        mp.osd_message("线性HDR已开启", 1.5)
    else
        mp.osd_message("❌ 恢复默认参数", 1.5)
    end
end

toggle_hdr()