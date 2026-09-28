# Cosy Games — website

Public multilingual website for [Cosy Games](https://cosygames.app/), an offline
Android games collection. English at `/`, French at `/fr/`, Spanish at `/es/`.
The Android app is maintained separately in a private repository. This repository
contains only the website and the public resources it needs.

## Local development

Requirements: Ruby 3.3, Bundler, Python 3.10+ for validation.

```sh
bundle install
bundle exec jekyll build
python3 check.py
bundle exec jekyll serve --host 127.0.0.1 --port 7358
```

Open http://127.0.0.1:7358/fr/. Jekyll builds to `build/site/`.

- `_data/content.json`: English, French and Spanish text.
- `_config.yml`: domain, public contact, policy date and editorial review flag.
- `_layouts/` and `_includes/`: Liquid templates and original game miniatures.
- `assets/`: styles, app icon and local Roboto fonts. Font license: `assets/LICENSE.txt`.
- Game miniatures reproduce the app home screen, including localised examples.
  Keep their composition and palette in sync when the app artwork changes.

## Deployment

Each push to `main` builds, validates and deploys the site to GitHub Pages.
Pull requests validate without deploying. A manual run from `main` can redeploy.
Only `build/site/` is uploaded, never the source tree. Enable GitHub Actions as the
Pages publishing source and set the custom domain to `cosygames.app`.

Configure the domain DNS for GitHub Pages, then enforce HTTPS when the certificate
is available. Preserve email DNS records. See the official
[custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

The privacy text remains a draft. `publication_reviewed: false` keeps a visible
notice and `noindex` even in production, without blocking deployment. Complete the
publisher details, review the three policies and confirm the contact mailbox
before setting it to true. This flag is an editorial status, not legal certification.
Contact: contact@cosygames.app.

No visitor-side JavaScript, analytics, cookies or external font requests.
GitHub Pages may process IP addresses for security as explained in the policy.
