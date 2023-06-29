## Why use Github wiki for documentation?

Pros:
1. Have full audit/version history
2. Biases towards making changes/updates without incurring friction from the PR flow.  Documentation is an area that usually is less catastrophic if you mess up and also something developers take less enjoyment out of.  As a result, it makes sense to remove barriers here.
3. Can easily edit with multiple interfaces (including Github GUI)
4. Renders a highly visible table of contents by default so we don't spend time doing this manually or agreeing on the markdown tool to do it for us.
5. Lives within Github where all the rest of the development work is done (no separate tool).
6. Can easily link to sub-sections of a document

➖ Cons:
1. Doesn't allow inline commenting.
2. Not self-service for the community to contribute changes for review under PR.  
3. One can't easily get notifications of changes by "watching" the repo.
4. There is no way to organize pages with sorting or [directories](https://stackoverflow.com/questions/11088285/github-wiki-directories)
5. While a strength above, it means that an accompanying documentation can't be in the PR for making a change
6. Renaming a page causes all existing links to break.

Other options that were considered:
* Notion
  -  Nice editing interface for making more polished docs
  -  Inline commenting capability
  -  Notifications
  -  Seamless rename handling
  - ➖ Separate tool outside of github
  - ➖ Version history and revert isn't as clear/precise as with git
* Markdown files in a "docs" directory
  -  Stay within github
  -  Notification of changes
  - ➖ Friction of PR flow since we protect the main branch
  - ➖ Github rendering isn't as good since don't get nice/clear table of contents
* Github issues as docs
  -  Stay within github
  - ~ Can add comments to the stream
  - ➖ Can't link to specific sections within text (can only link to a specific comment)
  - ➖ Clutters issue tracker and inflates the number of "open" issues

Examples of good github wikis: https://github.com/MyHoneyBadger/awesome-github-wiki

## What documentation is in scope?
In scope: anything that isn't catastrophic if it's off.

Out of scope:
1. API Docs

## When is Notion used?
Maintainers that are on the PL EngRes team [sometimes use Notion for one-offs](https://pl-strflt.notion.site/Helia-3cd11e7c9e7d491c93c96d6893aedb65).  This usually happens when need the features of Notion (inline commenting, databases).  In general though we want to default to create content in GitHub for easier discoverability.