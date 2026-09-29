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
- `_data/information.json`: translated support and legal pages.
- `_data/publisher.json`: confirmed public publisher details; omitted fields remain unpublished.
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

## Google Play publication pages

All pages exist in English (root), French (`/fr/`) and Spanish (`/es/`).

| Page | English URL | Purpose |
| --- | --- | --- |
| Privacy policy | `https://cosygames.app/privacy/` | App storage, website hosting, support contact, security and deletion |
| Help and contact | `https://cosygames.app/support/` | Support and Android local-data deletion instructions at `#delete-data` |
| Legal notice | `https://cosygames.app/legal/` | Publisher identity, hosting and resource credits |

Implemented: translated pages, footer navigation, language-preserving links and
local-data deletion instructions. No account-deletion form is provided because
the app does not create accounts. Google Play purchases are active in the internal test release; a transaction has
been tested successfully. The draft policy documents local life packs
and restoration of unlimited lives. No publisher identity or terms of sale are invented.

Before store submission:

- Confirm the publisher's country and legal status, then complete the applicable
  identity, address, contact and registration fields in `_data/publisher.json`.
  A personal Google Play account does not determine the legal status of the site.
- Review publisher and hosting disclosures under the applicable law (including
  hosting telephone details where required). Confirm support mailbox operation,
  its provider, retention criteria and the corresponding privacy wording.
- Review all three translations against the exact release build; remove the
  draft status only after this review. Enable and verify public HTTPS access.
- Add a privacy-policy link or text inside the Android app and the policy URL in
  Play Console. Complete the separate Data safety declaration from the actual
  release behavior, including every SDK; publishing these pages does not replace it.
- Reassess the policy and declarations before changing payments or enabling ads or accounts.

Reference requirements, checked on 28 September 2026:
[Google Play user data policy](https://support.google.com/googleplay/android-developer/answer/10144311?hl=en),
[account deletion](https://support.google.com/googleplay/android-developer/answer/13327111?hl=en),
[French professional website notices](https://entreprendre.service-public.gouv.fr/vosdroits/F31228),
[GitHub privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
Legal obligations depend on the publisher's confirmed status and jurisdiction.

No visitor-side JavaScript, analytics, cookies or external font requests.
GitHub Pages may process IP addresses for security as explained in the policy.

## Publication review — 29 September 2026

Public naming confirmed: use **Cosy Games** for the product and the app privacy
policy, **Stefan Cosquer** where the publisher's legal identity is required.
Country: France. The publisher describes their current status as an individual;
do not infer a company, registration number or exemption from commercial duties.
Contact mailbox confirmed operational: contact@cosygames.app, hosted by Gmail.
No personal postal address or telephone has been approved for publication.

The FR/EN/ES drafts now describe active Google Play purchases, local receipts,
Billing diagnostics, Gmail support and children aged 9 and above. The official
Billing release notes document diagnostic logging; the app dependency audit
also found device/system/network context in DataTransport. These texts are not
a claim that the publisher receives gameplay telemetry.

Still pending before removing the draft flag: settle the applicable publisher
address/status disclosures for an app offering paid digital goods, review the
support retention practice, and finish the Play Data safety declaration. Do not
replace the missing legal details with a brand or invent a public address.
