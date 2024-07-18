# from core.app import Database


# class DashboardManager:
#     def __init__(self):
#         self.db = Database()
#         self.guild_settings = self.db.DB.guild_settings

#     def get_guild_settings(self, guild_id):
#         guild_settings = self.guild_settings.find_one({"_id": guild_id})
#         if not guild_settings:
#             guild_settings = {"_id": guild_id, "lang": "en", "branch_channel": None, "log_channel": None}
#             self.guild_settings.insert_one(guild_settings)
#         return guild_settings

#     def update_guild_settings(self, guild_id, settings):
#         self.guild_settings.update_one({"_id": guild_id}, {"$set": settings})