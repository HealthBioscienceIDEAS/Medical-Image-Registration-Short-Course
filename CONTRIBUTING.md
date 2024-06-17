## Contributing

[The Carpentries][cp-site] ([Software Carpentry][swc-site], [Data
Carpentry][dc-site], and [Library Carpentry][lc-site]) are open source
projects, and we welcome contributions of all kinds: new lessons, fixes to
existing material, bug reports, and reviews of proposed changes are all
welcome.

### Contributor Agreement

By contributing, you agree that we may redistribute your work under [our
license](LICENSE.md). In exchange, we will address your issues and/or assess
your change proposal as promptly as we can, and help you become a member of our
community. Everyone involved in [The Carpentries][cp-site] agrees to abide by
our [code of conduct](CODE_OF_CONDUCT.md).

### How to Contribute

The easiest way to get started is to file an issue to tell us about a spelling
mistake, some awkward wording, or a factual error. This is a good way to
introduce yourself and to meet some of our community members.

1. If you do not have a [GitHub][github] account, you can [send us comments by
   email][contact]. However, we will be able to respond more quickly if you use
   one of the other methods described below.

2. If you have a [GitHub][github] account, or are willing to [create
   one][github-join], but do not know how to use Git, you can report problems
   or suggest improvements by [creating an issue][issues]. This allows us to
   assign the item to someone and to respond to it in a threaded discussion.

3. If you are comfortable with Git, and would like to add or change material,
   you can submit a pull request (PR). Instructions for doing this are
   [included below](#using-github).

Note: if you want to build the website locally, please refer to [The Workbench
documentation][template-doc].

### Where to Contribute

1. If you wish to change this lesson, add issues and pull requests here.
2. If you wish to change the template used for workshop websites, please refer
   to [The Workbench documentation][template-doc].


### What to Contribute

There are many ways to contribute, from writing new exercises and improving
existing ones to updating or filling in the documentation and submitting [bug
reports][issues] about things that do not work, are not clear, or are missing.
If you are looking for ideas, please see [the list of issues for this
repository][repo], or the issues for [Data Carpentry][dc-issues], [Library
Carpentry][lc-issues], and [Software Carpentry][swc-issues] projects.

Comments on issues and reviews of pull requests are just as welcome: we are
smarter together than we are on our own. **Reviews from novices and newcomers
are particularly valuable**: it's easy for people who have been using these
lessons for a while to forget how impenetrable some of this material can be, so
fresh eyes are always welcome.

### What *Not* to Contribute

Our lessons already contain more material than we can cover in a typical
workshop, so we are usually *not* looking for more concepts or tools to add to
them. As a rule, if you want to introduce a new idea, you must (a) estimate how
long it will take to teach and (b) explain what you would take out to make room
for it. The first encourages contributors to be honest about requirements; the
second, to think hard about priorities.

We are also not looking for exercises or other material that only run on one
platform. Our workshops typically contain a mixture of Windows, macOS, and
Linux users; in order to be usable, our lessons must run equally well on all
three.

### Using GitHub

#### Committing and pushing changes 
1. Clone this repo 
```
git clone git@github.com:UCL/real-time-ai-for-surgery.git
``` 
2. Create new branch using issue number
```
git checkout -b ISSUENUMBER-branch-name 
```
3. Commit changes and push to your branch
```
git add .
git commit -m 'short message (#ISSUENUMBER)'
git push origin ISSUENUMBER-branch-name
```
4. Submit a Pull Request against the `main` branch. 

#### Pull Request (PR) and merge to `main` branch
1. Select branch that contain your commits.
2. Click `Compare and pull request` and create PR for the associated branch.
3. Type a title and description of your PR and create PR
4. Please keep your PR in sync with the base branch.
```
git checkout main
git pull origin main
git checkout FEATURE_BRANCH
git rebase main
git push --force origin FEATURE_BRANCH
```
4.1 In case you are in a different `MY_FEATURE_BRANCH` branch, follow:
```
git checkout FEATURE_BRANCH
git pull origin FEATURE_BRANCH
git checkout MY_FEATURE_BRANCH 
git rebase FEATURE_BRANCH
git push --force origin MY_FEATURE_BRANCH
```
5. Run `pre-commit` to tidy up code and documentation (see next section). 
6. Request a PR review.
See [collaborating-with-pull-requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests) for further details.
7. Once your PRs has been approved, procced to merge it to main. See [Merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request)
8. Remove your merged branch from your repo and in the list of https://github.com/UCL/real-time-ai-for-surgery/branches
```
#Local git clear
git branch --merged | grep -v '\*\|master\|main\|develop' | xargs -n 1 git branch -d
#Remote git clear
git branch -r --merged | grep -v '\*\|master\|main\|develop' | sed 's/origin\///' | xargs -n 1 git push --delete origin
```

NB: The published copy of the lesson is usually in the `main` branch.

Each lesson has a team of maintainers who review issues and pull requests or
encourage others to do so. The maintainers are community volunteers, and have
final say over what gets merged into the lesson.

### Other Resources

The Carpentries is a global organisation with volunteers and learners all over
the world. We share values of inclusivity and a passion for sharing knowledge,
teaching and learning. There are several ways to connect with The Carpentries
community listed at <https://carpentries.org/connect/> including via social
media, slack, newsletters, and email lists. You can also [reach us by
email][contact].

[repo]: https://example.com/FIXME
[contact]: mailto:team@carpentries.org
[cp-site]: https://carpentries.org/
[dc-issues]: https://github.com/issues?q=user%3Adatacarpentry
[dc-lessons]: https://datacarpentry.org/lessons/
[dc-site]: https://datacarpentry.org/
[discuss-list]: https://carpentries.topicbox.com/groups/discuss
[github]: https://github.com
[github-flow]: https://guides.github.com/introduction/flow/
[github-join]: https://github.com/join
[how-contribute]: https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github
[issues]: https://carpentries.org/help-wanted-issues/
[lc-issues]: https://github.com/issues?q=user%3ALibraryCarpentry
[swc-issues]: https://github.com/issues?q=user%3Aswcarpentry
[swc-lessons]: https://software-carpentry.org/lessons/
[swc-site]: https://software-carpentry.org/
[lc-site]: https://librarycarpentry.org/
[template-doc]: https://carpentries.github.io/workbench/
