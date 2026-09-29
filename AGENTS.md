# Website development

- This public repository contains only the Cosy Games website. Never copy the
  private app repository, its Git history, game dictionaries, APKs or user data here.
- Read README.md before editing. Use Jekyll with the locked Ruby dependencies.
- Keep English, French and Spanish content in sync. Preserve the locale when
  switching between home, privacy, support and legal pages.
- Keep the monochrome, responsive design, system theme, local fonts and SVG
  miniatures. The editorial website can scroll vertically; no animation is needed.
- The game illustrations match the app home screen, including the words used in
  each language. They are decorative, not screenshots of real saved games.
- No analytics, cookies, third-party scripts or fabricated store/download links.
- Never describe the privacy policy as reviewed while publication_reviewed is false.
- Do not infer or publish the publisher's personal details. Use only explicitly
  confirmed public details in _data/publisher.json. Keep legal and privacy pages
  marked as drafts until the pending publication checks in README.md are resolved.
- After edits, run bundle exec jekyll build, python3 check.py, and inspect affected
  layouts in the browser. Do not add Flutter dependencies to this repository.
- Every push to main deploys the site after validation; PRs never deploy. Publish
  only build/site/. Do not commit build output, installed gems or caches.
- Communicate in French and distinguish local checks from public deployment.
