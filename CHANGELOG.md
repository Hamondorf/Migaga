# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [4.6.1] - 2021-02-03
### Fixes
- The leaderboard now only shows the top 5 users by points.
- Fixed dev configuration being put on live.

## [4.6.0] - 2021-02-03
### Features
- Added a !leaderboard command to show users with the most points in a guild. 
  
### Tweaks
- Updated discord.py version.
- Tweaked points formatting.

### Fixes
- Fixed requests to Discord intents.
- Fixed a crash when cleaning the Starboard and finding deleted messages.

## [4.5.1] - 2020-09-12
### Fixes
- Tweaked GitHub actions.
- Changed the emoji sent into the #long-dair channel.

## [4.5.0] - 2020-09-12
### Features
- The !ban command will now check users globally by ID.

### Server Config
Introducing configuration options so that a server can have more control over how the bot works. 
Use !help config to get started.
- Server logs no longer write logs to whatever channel it finds named #server-logs. The channel must now be configured.
- Starboard emoji can now be configured using the server configuration. 
- Points name and points emoji have been moved to the server config.

## [4.4.1] - 2020-08-22
### Features
- Added some aliases to the `search` command and expanded its use to allow showing all custom commands. 
- Added a `!massban` command for admins which will also search for users based on the ID.
- Added some requested aliases to common admin commands.

### Maintenance
- The bot is now running on Docker in production.

## [4.4.0] - 2020-08-08
### Points
- Added a configurable way for guild owners to add or remove points from members of their guild.
- Users can see their own or others points. 
- Points can be given a configurable name and emoji.

### Maintenance
- Improved logging for reminders and the starboard.
- Reduced the amount of time a starboard message is "cleaned up" for.

## [4.3.1] - 2020-07-27
### Maintenance
- Added logging configuration to source control. 
- Added deployment ecosystem for pm2.

## [4.3.0] - 2020-07-26
### Features
- Changed the display of the help command.
- Re-introduced the "remindme" command.

### Fixes
- Fixed a bug that would stop starboard processing for older messages.

## [4.2.0] - 2020-07-25
### Features
- Welcome messages can now be deleted from servers.
- Changed the look and feel of starboard messages. 
- Servers can now set thresholds for starred messages that will have them swept from the channel.

## [4.1.1] - 2019-10-01
### Fixes
- Added error reporting for when the user calls a command they don't have permissions for.
- Fixed a bug which caused the reminder date to be formatted incorrectly when confirming reminders.

### Database
- Refactored the database connection so that it keeps itself alive. 

## [4.1.0] - 2019-09-23
### Role Flairing
- Provided admin commands for adding and removing role flairs from a message.
- When a user reacts to a message configured with a role flair they will be given the roles recorded against that message.
- If a role has overwrites set up against it then the other roles will be removed when reacting.
- Added helper commands for finding information on reaction flairs.

### Commands
- Added a new command for removing fields from your profile.

### Fixes
- Fixed a bug which caused the removal of stars to be missed by the bot.
- Fixed a bug in the !invite command.

### Tweaks
- Changed the way database connections are managed in the event that the connection is dropped.

## [4.0.1] - 2019-09-21
### Features
- Now actually assign and remove roles based on the `!addrole` and `!overwrite` commands on message.
- Added the `!emoji` command to get a larger version of an emoji. 
- Removed the need to save changed avatars and icons to local storage.
- Changed the formatting on the Starboard.

## [4.0.0] - 2019-09-21
### Global
- Cleaned up the code a lot - you should see some performance improvements.
- With cleaner code comes greater extendability so features can be released quicker.
- Updated to use Discord.py API latest (v1.2.3).
- Updated to Python 3.7.
- Moved to a GCP database.
- Improved error reporting to the user.
- Improved command error reporting to me. 
- Removed the original logging implementation. 

### Server Logs
- Redesigned the majority of server log messages.
- Added logging for deleted images.
- Added logging for avatar changes.
 
### Games & Fun
- Removed money from games. This may be replaced in the future! Just not now.
- Fixed crashes on some games.
- Fixed a bug which would cause the choose command to give a malformed response when separating with spaces.
- Fixed the cat command!

### Starboard
- Users can no longer star themselves.
- Changed the look and feel of Starboard messages,

### Admin
- Admin commands now resolve users through ID, name, etc.
- A guild can now have multiple welcome messages.
- Fixed role overwrites.

### Profiles
- The bot now supports configured profiles with custom fields.
- Added more helpful documentation on command usage.

### Reminders
- Added a new command for making reminders in the future based on a date.
- Added the ability to remind channels and users rather than posting in the original channel.
- Reminders are now more robust. They can be queued and sent when the bot reconnects.