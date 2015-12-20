# Change Log

## [0.1](https://github.com/waartaa/ircb/tree/0.1) - 2015-12-20

This is the inital releas for **ircb** and ships with the following features:
- Allow multiple simultaneous client connection for a IRC network connection
- Support SSL connection to IRC server
- Basic CLI to create users, networks
- Autojoin previously joined channels on re connecting to IRC network

**Implemented enhancements:**

- Autojoin previously joined channels when connected to IRC server [\#27](https://github.com/waartaa/ircb/issues/27)
- Add support for ssl, ssl\_verify fields in "ircb networks create" command [\#22](https://github.com/waartaa/ircb/issues/22)
- Connect to IRC server using SSL [\#18](https://github.com/waartaa/ircb/issues/18)
- Allow SSL connection to IRC networks [\#17](https://github.com/waartaa/ircb/issues/17)
- Dynamically generate IRC joining messages for clients when reusing existing IRC connection [\#11](https://github.com/waartaa/ircb/issues/11)

**Fixed bugs:**

- Don't send ChoiceType field in IrcbBot config for network for ssl\_verify [\#23](https://github.com/waartaa/ircb/issues/23)
- Fix handling multiple IRC clients for same bot [\#8](https://github.com/waartaa/ircb/issues/8)

**Closed issues:**

- ircb networks create does not work [\#20](https://github.com/waartaa/ircb/issues/20)
- Prevent race condition during two clients trying to connect to the same IRC network [\#15](https://github.com/waartaa/ircb/issues/15)
- Monthly release for ircb [\#10](https://github.com/waartaa/ircb/issues/10)
- Sent messages using IrcbIrcBot is prefixed with ':' [\#6](https://github.com/waartaa/ircb/issues/6)

**Merged pull requests:**

- Autojoin previously joined channels when connecting to IRC server. [\#28](https://github.com/waartaa/ircb/pull/28) ([rtnpro](https://github.com/rtnpro))
- Implemented: Add support for ssl, ssl\_verify fields in 'ircb networks create' command. issue \#22 [\#24](https://github.com/waartaa/ircb/pull/24) ([PolBaladas](https://github.com/PolBaladas))
- Fixed issue \#20 'ircb network create does not work' [\#21](https://github.com/waartaa/ircb/pull/21) ([PolBaladas](https://github.com/PolBaladas))
- Allow connecting to IRC server using SSL. Fixes \#18 [\#19](https://github.com/waartaa/ircb/pull/19) ([rtnpro](https://github.com/rtnpro))
- Fixes race condition during multiple clients connecting to same network [\#16](https://github.com/waartaa/ircb/pull/16) ([rtnpro](https://github.com/rtnpro))
- Dynamic irc join messages [\#14](https://github.com/waartaa/ircb/pull/14) ([rtnpro](https://github.com/rtnpro))
- Add local & remote socket info for a IRC network connection [\#13](https://github.com/waartaa/ircb/pull/13) ([rtnpro](https://github.com/rtnpro))
- Add alembic to manage migration [\#12](https://github.com/waartaa/ircb/pull/12) ([rtnpro](https://github.com/rtnpro))
- Improve handling of raw messages from IRC clients. Fixes \#6 [\#7](https://github.com/waartaa/ircb/pull/7) ([rtnpro](https://github.com/rtnpro))
- Use irc3 bot to interact with remote IRC server. [\#5](https://github.com/waartaa/ircb/pull/5) ([rtnpro](https://github.com/rtnpro))
- Added stores for ircb [\#4](https://github.com/waartaa/ircb/pull/4) ([rtnpro](https://github.com/rtnpro))
- minor typo fix in README [\#3](https://github.com/waartaa/ircb/pull/3) ([sayanchowdhury](https://github.com/sayanchowdhury))
- update the README for setting up ircb on dev environments [\#2](https://github.com/waartaa/ircb/pull/2) ([sayanchowdhury](https://github.com/sayanchowdhury))
- Update installation docs from pip to pip3 [\#1](https://github.com/waartaa/ircb/pull/1) ([sayanchowdhury](https://github.com/sayanchowdhury))

