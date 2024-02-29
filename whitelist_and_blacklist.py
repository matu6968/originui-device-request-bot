# This is the whitelist and blacklist system for the bot.
# It is used to prevent users from requesting unsupported devices, or used to allow certain models from blacklisted manufacturers.
# EVERYTHING HAS TO BE IN LOWERCASE!

# Put a manufacturer here to blacklist it.
phone_manufacturer_blacklist = {"imo", "in my opinion", "alcatel", "nokia", "microsoft", "tecno", "huawei", "ulefone", "tcl"}

# Put a device model here to whitelist it.
phone_model_whitelist = {
  "example": {"device 1", "device 2", "device 3"}, # etc.. (REMEMBER ABOUT THE COMMAS)
  "microsoft": {"surface pro duo", "surface pro duo 2"},
  "huawei": {"p20 lite", "p20", "p20 pro"}, 
}

phone_model_blacklist = {
  "example": {"device 1", "device 2", "device 3"}, # etc.. (REMEMBER ABOUT THE COMMAS)
  "huawei": {"nova 12", "nova 12 pro", "nova 12 ultra"},
}
