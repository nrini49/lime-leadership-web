#!/usr/bin/env python3
"""Generates the LIME Leadership static site pages from content data below."""
import html, re

LOGO_SVG = '''<svg width="26" height="26" viewBox="0 0 32 32" fill="none" aria-hidden="true">
<path d="M16 4c-3 4-6 7-6 12a6 6 0 0 0 12 0c0-5-3-8-6-12z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M16 14c-1.4 2-2.4 3.4-2.4 5.4a2.4 2.4 0 0 0 4.8 0c0-2-1-3.4-2.4-5.4z" fill="currentColor"/>
</svg>'''

NAV = [
    ("/", "Home"),
    ("/promises/", "Promises of Jesus"),
    ("/bezalel-promise/", "The Bezalel Promise"),
    ("/keepers/", "The Keepers"),
    ("/david-sang/", "David Sang"),
]

def rel(path_from, target):
    # both are site-root-relative paths like "/" or "/promises/"
    if target == "/":
        return ("../" * (path_from.count("/") - (1 if path_from.endswith("/") else 0))) or "./" if path_from != "/" else "./"
    return None

def page(title, description, body, current, depth):
    """depth = 0 for root index.html, 1 for /section/index.html"""
    root = "../" * depth if depth else "./"
    nav_html = []
    for href, label in NAV:
        target = (root + href.lstrip("/")) if href != "/" else root
        current_attr = ' aria-current="page"' if href == current else ""
        nav_html.append(f'<a href="{target}"{current_attr}>{label}</a>')
    nav_html = "\n        ".join(nav_html)
    css = root + "assets/css/style.css"
    js = root + "assets/js/theme.js"
    home_href = root
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}" />
<meta name="robots" content="index, follow" />
<meta name="color-scheme" content="light dark" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%2301696f'/%3E%3Cpath d='M16 6c-2.6 3.4-5.2 6-5.2 10.2a5.2 5.2 0 0 0 10.4 0C21.2 12 18.6 9.4 16 6z' fill='%23f7f6f2'/%3E%3C/svg%3E" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Work+Sans:ital,wght@0,300..700;1,300..700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="{css}" />
</head>
<body>
<a class="sr-only" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="wordmark" href="{home_href}">
      {LOGO_SVG}
      <span>LIME Leadership<br><span class="sub">Formation &amp; the Interpretive Bridge</span></span>
    </a>
    <nav class="site-nav" aria-label="Primary">
        {nav_html}
    </nav>
    <button class="theme-toggle" data-theme-toggle type="button" aria-label="Switch to dark mode"></button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <p>&copy; 2026 Lime Signalworks LLC. A LIME interpretive-bridge project.</p>
    <p><a class="sibling-link" href="https://limesignalworks.com" rel="noopener noreferrer">Lime Signalworks<span aria-hidden="true"> &#8599;</span></a></p>
  </div>
</footer>
<script src="{js}"></script>
</body>
</html>
"""

def esc(s):
    return html.escape(s, quote=False)

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
home_body = f"""
<section class="hero">
  <div class="wrap">
    <p class="eyebrow">LIME &middot; Leadership &amp; Formation</p>
    <h1>Guideposts for those<br>who carry the flame.</h1>
    <p class="lede">A working library of Scripture study, interpretive-bridge writing, and formation material &mdash; built one recognition at a time, and given away freely to whoever is ready for it.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="section-title">Start here</h2>
    <div class="card-grid">
      <a class="card" href="promises/">
        <span class="tag">Scripture Study</span>
        <h3>The Promises of Jesus</h3>
        <p>Guideposts from the Road to Life &mdash; a promise-by-promise study moving forward from John 1 toward the end of Revelation. Volumes I, II, &amp; III are ready now.</p>
        <span class="go">Read the volumes &rarr;</span>
      </a>
      <a class="card" href="bezalel-promise/">
        <span class="tag">Foundation</span>
        <h3>The Bezalel Promise</h3>
        <p>The founding promise of Lime Signalworks itself &mdash; honest work, loss-prevention first, and what happens when that promise doesn't hold.</p>
        <span class="go">Read the promise &rarr;</span>
      </a>
      <a class="card" href="keepers/">
        <span class="tag">Canon</span>
        <h3>The Keepers</h3>
        <p>Eight figures, eight doors &mdash; a working canon of biblical archetypes used to give the LIME system a human face.</p>
        <span class="go">Meet the Keepers &rarr;</span>
      </a>
      <a class="card" href="david-sang/">
        <span class="tag">Interpretation</span>
        <h3>David Sang: Energy-Language Interpretation</h3>
        <p>A guarded, line-by-line translation of a worship song into energy-language &mdash; keeping God prior and external at every step.</p>
        <span class="go">Read the interpretation &rarr;</span>
      </a>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <h2 class="section-title">Coming next</h2>
    <p style="color:var(--color-text-muted); max-width:60ch;">This library is still being built, in the open, one section at a time. Next up:</p>
    <ul class="roadmap">
      <li><span class="vol">Pastor &amp; Leader Training</span><span>A working wiki for those forming others, not just themselves.</span></li>
      <li><span class="vol">The Bridge Method</span><span>The glossary and prompt kit behind every interpretive bridge in this library.</span></li>
      <li><span class="vol">Multiverse Catalog</span><span>The fuller reference behind the metaphor language used throughout this work.</span></li>
    </ul>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# PROMISES OF JESUS
# ---------------------------------------------------------------------------
promises_body = f"""
<section class="hero" style="padding-bottom: var(--space-8);">
  <div class="prose-wrap">
    <p class="eyebrow">Scripture Study</p>
    <h1 style="font-size: var(--text-2xl);">The Promises of Jesus</h1>
    <p class="lede" style="font-size: var(--text-lg);">Guideposts from the Road to Life</p>
    <p class="prose" style="margin-top: var(--space-6);">Not a hunt for detached assurances, but an encounter with the character of Jesus &mdash; the One whose goodness gives every promise its meaning. This study moves forward canonically, beginning where John begins, walking toward the end of Revelation, one volume at a time.</p>
  </div>
</section>

<section style="padding-top:0;">
  <div class="prose-wrap">
    <div class="volume-card">
      <div>
        <h3>Volume I &mdash; The Gospel of John</h3>
        <p>Fifteen promises, from the right to become a child (John 1:12&ndash;13) to a blessing named for those who never touched the wounds and believed anyway (John 20:29).</p>
      </div>
      <a class="btn" href="../assets/pdf/The_Promises_of_Jesus_Volume_I.pdf">Read Volume I (PDF)</a>
    </div>
    <div class="volume-card">
      <div>
        <h3>Volume II &mdash; The Letters of John</h3>
        <p>Twelve promises across 1, 2, and 3 John &mdash; cleansing, abiding, confidence, and a truth named as permanent, already remaining, already guaranteed to stay.</p>
      </div>
      <a class="btn" href="../assets/pdf/The_Promises_of_Jesus_Volume_II.pdf">Read Volume II (PDF)</a>
    </div>
    <div class="volume-card">
      <div>
        <h3>Volume III &mdash; The Synoptic Gospels and Acts</h3>
        <p>Fourteen promises across Matthew, Mark, Luke, and Acts &mdash; the Kingdom, rest, forgiveness, prayer, and a promise poured out at Pentecost for whoever is far off and still being called.</p>
      </div>
      <a class="btn" href="../assets/pdf/The_Promises_of_Jesus_Volume_III.pdf">Read Volume III (PDF)</a>
    </div>

    <h3 class="sub-title">What comes next</h3>
    <ul class="roadmap">
      <li><span class="vol">Volume IV</span><span>The Epistles &mdash; adoption, perseverance, grace, transformation, hope.</span></li>
      <li><span class="vol">Volume V</span><span>Revelation &mdash; presence, renewal, healing, and &ldquo;Surely I am coming soon.&rdquo;</span></li>
    </ul>

    <div class="callout">
      <div class="label">How each promise is studied</div>
      Every entry follows the same seven-part frame: the text (World English Bible, public domain), speaker and audience, immediate meaning, Jesus&rsquo; revealed nature, an interpretive bridge into this project&rsquo;s metaphor language, an embodied response, and cross-references &mdash; kept in that order so Scripture stays the source and metaphor stays strictly secondary to it.
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# THE BEZALEL PROMISE
# ---------------------------------------------------------------------------
bezalel_body = f"""
<section class="hero" style="padding-bottom: var(--space-8);">
  <div class="prose-wrap">
    <p class="eyebrow">Foundation</p>
    <h1 style="font-size: var(--text-2xl);">The Bezalel Promise</h1>
    <p class="prose" style="margin-top: var(--space-6);">Bezalel was the craftsman the Lord filled with skill to build the tabernacle by hand &mdash; not by mysticism, but by real, honest, skilled work (Exodus 31:1&ndash;5). This is the promise that carries his name: the founding commitment of Lime Signalworks itself, stated plainly, with nothing oversold.</p>
  </div>
</section>

<section style="padding-top:0;">
  <div class="prose-wrap prose">
    <blockquote>
      <p>We cannot and do not guarantee profits or eliminate risk &mdash; no honest system can. Markets go up, down, and sideways, and your decisions and results are your own.</p>
    </blockquote>
    <p>What we do promise is our best work: clear teaching, honest tools, and a solid system built to serve real families and real companies by leaning first toward loss prevention, then toward profit. If that does not feel true in your experience after ninety days, you do not pay for it.</p>

    <h3 class="sub-title">Why it carries Bezalel&rsquo;s name</h3>
    <p>Bezalel was not chosen for charisma or self-promotion. He was chosen and equipped to build something real, with his hands, that would hold up under actual use &mdash; a craftsman&rsquo;s calling, not a performer&rsquo;s. That is the standard this promise holds itself to: build the honest thing, state its limits plainly, and let the ninety days of real use be the proof, not the pitch.</p>

    <div class="callout">
      <div class="label">Scope of this promise</div>
      This text originates as the founding promise language for Lime Signalworks&rsquo; product work. It is included here because it is a promise in the fullest sense &mdash; a stated commitment, kept accountable to a real time frame, offered without inflating what it can deliver.
    </div>
  </div>
</section>
"""

def keepers_row(door, content, role, keeper, why):
    return f"""      <tr>
        <td data-label="Door">{door}</td>
        <td data-label="Door content">{content}</td>
        <td data-label="Archetype role">{role}</td>
        <td class="keeper-name" data-label="Keeper">{keeper}</td>
        <td data-label="Why this fit">{why}</td>
      </tr>"""

keepers_rows_data = [
    ("01", "System Access &mdash; unlocks the personal Rosie sandbox", "The Guardian", "Peter", "Given the keys &mdash; &ldquo;I will give you the keys of the kingdom&rdquo; (Matthew 16:19)."),
    ("02", "What LIME Is &mdash; plain-language explainer", "The Sage", "Solomon", "Wisdom made practical and legible, not mystical."),
    ("03", "Bring Someone &mdash; personal invitation to the harbor", "The Herald", "Mary Magdalene", "She ran to tell the disciples &mdash; the original herald of resurrection, carrying announcement no one believed."),
    ("04", "Inner Rail / Fire Spirit &mdash; inner discipline into disciplined action", "The Contemplative", "Mary of Bethany", "She chose the one thing. Sat, listened, anointed at the exact right moment against all social pressure. Discipline as reception, not force."),
    ("05", "Situation Report &mdash; today&rsquo;s market weather, read before acting", "The Watchman", "Daniel", "Reads what others can&rsquo;t, stays composed and clear under real pressure."),
    ("06", "The Offer &mdash; what you get, what it costs, the terms", "The Intercessor", "Esther", "&ldquo;If I perish, I perish.&rdquo; Presented terms at the exact right moment at great personal risk to save her people."),
    ("07", "SPY Harbor Watch &mdash; the night-watch game, patience is the position", "The Shepherd", "Ruth", "Steadfast loyalty through the whole dark stretch, not leaving the post."),
    ("08", "The Laugh Lounge", "The Joker", "David", "Wit and heart together &mdash; danced unashamed."),
]
keepers_rows = "\n".join(keepers_row(*r) for r in keepers_rows_data)

keepers_body = f"""
<section class="hero" style="padding-bottom: var(--space-8);">
  <div class="prose-wrap">
    <p class="eyebrow">Canon</p>
    <h1 style="font-size: var(--text-2xl);">The Keepers</h1>
    <p class="prose" style="margin-top: var(--space-6);">A set of 8 figures, drawn from a larger set of 22, giving each of the Eight Harbor Doors a human face. Each of the 22 pairs an archetype role with a biblical figure who embodies it &mdash; a worked example, not an oracle. Only the 8 that fit the current doors are defined here; the rest remain undefined until they&rsquo;re needed.</p>
  </div>
</section>

<section style="padding-top:0;">
  <div class="wrap">
    <table class="keepers-table">
      <thead>
        <tr><th>Door</th><th>Door content</th><th>Archetype role</th><th>Keeper</th><th>Why this fit</th></tr>
      </thead>
      <tbody>
{keepers_rows}
      </tbody>
    </table>

    <div class="prose-wrap" style="padding-inline:0; margin-top: var(--space-10);">
      <p class="prose">Four women, four men: Mary Magdalene, Mary of Bethany, Esther, and Ruth; Peter, Solomon, Daniel, and David. Door 08 (The Laugh Lounge) exists specifically to give David&rsquo;s fit &mdash; the Joker, humor and heart together &mdash; a real home, rather than forcing him onto a door he doesn&rsquo;t belong on.</p>
      <div class="callout">
        <div class="label">On the name &ldquo;Keepers&rdquo;</div>
        The 22 are deliberately not called &ldquo;Arcana&rdquo; &mdash; that word carries tarot and occult association this project explicitly avoids, especially for Christian readers encountering the site. &ldquo;Keepers&rdquo; is the chosen term throughout.
      </div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------------------
# DAVID SANG: ENERGY-LANGUAGE INTERPRETATION
# ---------------------------------------------------------------------------
pairs_data = [
    ("Heaven opens from inside", "The stars were still above the field when David knelt and spoke... Before the sun rose, he believed. Heaven was already moving... Heaven opens from inside.", "Before the world was awake to confirm it, David tuned in and spoke. Before he had any evidence, he held the frequency &mdash; because the field was already shifting to meet him. The opening doesn&rsquo;t happen out there. It happens in the alignment first, then shows up outside."),
    ("The provision frequency (&ldquo;God provides&rdquo;)", "He declared your open hand over every empty place... Every morning he would sing, God provides, God provides.", "Every morning he tuned back into the one unlimited source and named it over every gap in his life. He wasn&rsquo;t generating supply out of his own will &mdash; he was resyncing with a supply that was already broadcasting, whether he noticed it or not."),
    ("Favor precedes the step", "Favor follows every step I take. God has gone before this road.", "The path was already energetically cleared before he set foot on it. Favor isn&rsquo;t something you manufacture by trying harder &mdash; it&rsquo;s the wake left behind by a Source that moved first. He walked into an alignment already prepared, not toward one he had to build."),
    ("Doors opened by favor, not striving", "There are doors that no hand opens, no amount of striving earns... Heaven opens every door before me, by the favor of the Lord alone.", "Some doors don&rsquo;t respond to effort or hustle-energy at all &mdash; they only respond to alignment. He named plainly that willpower wasn&rsquo;t the mechanism. The opening came from the Source&rsquo;s own initiative; his part was positioning, not forcing."),
    ("No lack in the design (Psalm 23)", "The Lord is my shepherd, I shall not want... He prepares the table, pours the wine, every need alive with his design.", "He wasn&rsquo;t manifesting abundance from scratch &mdash; he was resting inside a design that was never built around lack to begin with. The table was already set before he arrived at it. His only work was to trust the design and take his seat."),
    ("The Name as a fixed point of supply", "Jehovah Jireh, on the mountain, you provide... Your hand has never once run dry. Your covenant holds the supply.", "He anchored to a fixed frequency of provision that doesn&rsquo;t fluctuate with circumstance &mdash; the way you&rsquo;d lock onto a signal instead of trying to generate your own. That anchor point, not his own effort, is what held the supply steady."),
    ("Overflow beyond the need (Psalm 23:5)", "He prepared a table in the presence of every trial... My cup overflows with your abundance, more than I could carry on my own.", "The overflow showed up in the middle of pressure, not after it cleared &mdash; proof it wasn&rsquo;t self-generated from his own good mood or effort. More came through than he could have produced by will alone, which is exactly how you know the source of it wasn&rsquo;t him."),
    ("Declaring the rain before the clouds", "The ground had been expecting rain long before the clouds arrived... Not by forecast, not by feeling, but by covenant I stand.", "He spoke the outcome while there was still zero visible evidence for it &mdash; not from optimism or mood, but because he trusted an agreement that existed prior to any sign. He called this standing on something already settled, not something he was willing into being."),
    ("Growth on the Source&rsquo;s timing, not his own", "Seeds I planted in the field of faith are growing by his faithful hand... blooming on his schedule, not my plan.", "He planted the seed of trust and then let go of the timeline. The growth was happening on a schedule set by the field itself, not by his own urgency or a self-imposed deadline. Forcing the timing would have worked against the very alignment he was counting on."),
    ("The word that outlasts appearances", "The God who keeps his ancient word is keeping it today... He does not forget the covenant. He does not lose the thread.", "What was set in motion doesn&rsquo;t decay with time or lose its charge. The agreement behind his current reality was made long before his current circumstances existed, and it doesn&rsquo;t need him to keep re-manifesting it &mdash; it&rsquo;s already self-sustaining."),
    ("Breakthrough already in motion", "I can feel the ground beginning now to shift... Breakthrough is already on the way. A financial miracle across the open ocean.", "The shift in the atmosphere came before the shift in his bank account &mdash; he felt the frequency change first. The breakthrough wasn&rsquo;t something he pushed into existence; it was already moving toward him, and what he felt was the field rearranging ahead of the visible result."),
    ("Trust as the posture during the gap", "I trust the God of every promise, the faithful one who does not change... I will wait with open hands.", "In the space between intention and manifestation, his only job was steady trust, not strain. Open hands, not gripping hands. The waiting itself wasn&rsquo;t wasted time &mdash; it was the posture that kept him aligned while the unseen mechanism did its work."),
    ("Responsive heaven, not self-powered heaven", "Heaven moves when faithful hearts believe... not because my faith is great or perfect, but because his faithfulness is sure.", "Belief doesn&rsquo;t generate the outcome by its own power &mdash; it&rsquo;s the receiver being tuned correctly so the signal that was already transmitting can land. The strength wasn&rsquo;t in his own believing; the reliability was on the other end of the connection, not in him."),
    ("Favor pre-positioned in rooms not yet entered", "Favor is waiting just up ahead... The people we meet may carry a key to open a door we never could find.", "The connections and opportunities were already placed in his path before he walked into the room. He wasn&rsquo;t attracting people toward him through personal magnetism &mdash; the alignment had already been arranged on both ends before the meeting happened."),
    ("Seen before spoken", "He sees the need before I speak. He moves before I call.", "The response was already initiated before he even voiced the intention. This is the clearest place the original breaks from typical energy-language causality: it&rsquo;s not &ldquo;ask and the universe responds&rdquo; &mdash; it&rsquo;s &ldquo;you were already known and already being met, and your asking is you catching up to what was already moving.&rdquo;"),
    ("Singing before the miracle arrives", "He sang before the miracle arrived. He praised before the open door appeared... Singing first will call the morning light.", "The declaration came first in sequence, but not first in cause. He sang in response to a promise he trusted was already real, not to manufacture one that wasn&rsquo;t. The song tuned him to what already existed on the frequency &mdash; it didn&rsquo;t invent the frequency."),
    ("Breakthrough by shout, not by force (Jericho)", "Like walls of Jericho that fell not by a sword but by a shout... I do not need to force the door. I stand in faith and let him move.", "The old pattern didn&rsquo;t collapse through pressure or strategy &mdash; it collapsed through an aligned, released declaration paired with something happening on a level beyond ordinary cause and effect. Force and forcing your will are the opposite move from the one that actually worked here."),
    ("The declared mechanism itself", "Heaven responds to faith declared in trust. God has promised and his promise stands and must.", "It isn&rsquo;t the intensity or repetition of the declaration that moves anything. What moves is trust directed at something that was already promised. Declaration is the tuning fork, not the generator."),
    ("The word that always lands (Isaiah 55 echo)", "His word never returns to him empty... What he said above my life is on its way.", "Once something true was spoken over his life from the source, it kept moving toward completion on its own &mdash; it didn&rsquo;t need to be re-charged by his continual belief to keep functioning. The signal, once sent, doesn&rsquo;t degrade in transit."),
    ("Seen in the dark before being answered", "Jehovah Jireh saw the singer in the dark... and answered every prayer before it was deferred.", "Being witnessed came before being answered &mdash; in the hidden, unglamorous seasons where no one else could see the effort. The alignment was already registered even when there was no external evidence of it yet."),
    ("Identity anchored in relationship, not self-declaration", "Jehovah Jireh, your name is my portion... every time I say it, something opens.", "His identity and inheritance were anchored to relationship with the Source, not to a self-made identity statement. Saying the name opened something specifically because of what &mdash; or who &mdash; was on the other side of it, not a private frequency he personally generated by repeating a phrase."),
    ("Generational track record", "Faithful God, you have provided always... through every season, through every long and patient wait.", "The pattern has a track record that predates him and will outlast him. Trusting it isn&rsquo;t naive optimism &mdash; it&rsquo;s pattern-recognition applied to something that has already proven consistent across time."),
    ("Closing image &mdash; windows already opening (Malachi 3:10 echo)", "The windows of heaven are opening now... The windows are open. The rain is falling. Heaven is moving. And I am receiving.", "The final posture is receiving, not producing. The opening already happened on the Source&rsquo;s side; what changed for him was noticing it and letting it land. That&rsquo;s the whole arc, start to finish: tune in, trust what&rsquo;s already true, then receive what was never actually withheld."),
]

def pair_html(i, title, original, energy):
    return f"""    <div class="pair">
      <span class="pair-num">{i:02d}</span>
      <h3>{title}</h3>
      <div class="pair-grid">
        <div class="pair-col original">
          <div class="label">Original</div>
          <p>&ldquo;{original}&rdquo;</p>
        </div>
        <div class="pair-col energy">
          <div class="label">Energy language</div>
          <p>{energy}</p>
        </div>
      </div>
    </div>"""

pairs_html = "\n".join(pair_html(i, t, o, e) for i, (t, o, e) in enumerate(pairs_data, 1))

david_sang_body = f"""
<section class="hero" style="padding-bottom: var(--space-8);">
  <div class="prose-wrap">
    <p class="eyebrow">Interpretation</p>
    <h1 style="font-size: var(--text-2xl);">David Sang This Every Morning</h1>
    <p class="lede" style="font-size: var(--text-lg);">An Energy-Language Interpretation</p>
    <p class="prose" style="margin-top: var(--space-6);">Source: <a href="https://www.youtube.com/watch?v=r_oku3x_FfY">David Sang This Every Morning for His Financial Miracle</a>, Open Heavens Psalms. Paired by movement using the LIME Bridge Method &mdash; one representative pairing per movement covers the full 2:26:21 arc.</p>
    <div class="callout">
      <div class="label">Guardrail this pass follows</div>
      Energy language may describe the human posture as alignment, attunement, or receiving &mdash; never as self-generation. Every line below keeps Source/Field prior and external to the speaker, exactly as the original keeps God prior and external to David. No line says &ldquo;I am the source&rdquo; or &ldquo;I create my reality.&rdquo; Where the original says God provides, opens, or moves, the energy-language version says the Field/Source already does &mdash; the human still only aligns, declares, and receives. &ldquo;Multiverse&rdquo; does not appear anywhere below, per instruction.
    </div>
  </div>
</section>

<section style="padding-top:0;">
  <div class="prose-wrap">
{pairs_html}

    <h3 class="sub-title">Where the mapping got strained</h3>
    <div class="prose">
      <p><strong>Names and proper nouns</strong> (Jehovah Jireh, Abraham, David, Jericho) have no clean energy-language equivalent &mdash; they&rsquo;re specific historical/relational anchors, not transferable concepts. They were kept as &ldquo;the Source,&rdquo; &ldquo;an ancient pattern,&rdquo; or footnoted, rather than inventing a fake substitute for a name.</p>
      <p><strong>Pairs 15 and 18</strong> are the two places where the original&rsquo;s actual claim &mdash; you are known and answered before you declare; declaration is response, not cause &mdash; sits in real tension with how energy-language content usually frames manifestation. That tension was named, not softened, because collapsing it would misrepresent both sides.</p>
      <p><strong>&ldquo;Covenant&rdquo;</strong> doesn&rsquo;t map cleanly to anything in energy language that isn&rsquo;t either too legal (&ldquo;contract&rdquo;) or too vague (&ldquo;agreement&rdquo;). &ldquo;Agreement,&rdquo; &ldquo;promise,&rdquo; and &ldquo;pattern&rdquo; were used depending on context rather than one fixed substitute.</p>
    </div>
  </div>
</section>
"""

pages = [
    ("index.html", "LIME Leadership \u2014 Formation & the Interpretive Bridge",
     "A working library of Scripture study, interpretive-bridge writing, and formation material from Lime Signalworks.",
     home_body, "/", 0),
    ("promises/index.html", "The Promises of Jesus \u2014 LIME Leadership",
     "Guideposts from the Road to Life: a promise-by-promise study moving forward from John 1 toward Revelation.",
     promises_body, "/promises/", 1),
    ("bezalel-promise/index.html", "The Bezalel Promise \u2014 LIME Leadership",
     "The founding promise of Lime Signalworks: honest work, loss-prevention first, ninety days of proof.",
     bezalel_body, "/bezalel-promise/", 1),
    ("keepers/index.html", "The Keepers \u2014 LIME Leadership",
     "A working canon of eight biblical archetypes giving the LIME system's Eight Harbor Doors a human face.",
     keepers_body, "/keepers/", 1),
    ("david-sang/index.html", "David Sang: Energy-Language Interpretation \u2014 LIME Leadership",
     "A guarded, line-by-line energy-language interpretation of David Sang's Open Heavens Psalms, keeping God prior and external.",
     david_sang_body, "/david-sang/", 1),
]

import os
BASE = os.path.dirname(os.path.abspath(__file__))
for filename, title, desc, body, current, depth in pages:
    out_path = os.path.join(BASE, filename)
    with open(out_path, "w") as f:
        f.write(page(title, desc, body, current, depth))
    print("wrote", out_path)
