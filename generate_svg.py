import html

raw_lines = [
'           ........:::::::            ',
'           .-=----::...:::            ',
'           %@@@@@@@@%=-..:            ',
'          #@@@@@@@@@@@@%:.            ',
'         @@@@@@@@@@@@@@@@=            ',
'        @@@@@@@@@@@@@@@@@@            ',
'      +@@@@@@@@@@@@@@@@@@@#           ',
'      @@@@@@@@@@@@@@@@@@@@@           ',
'     #@@@@@@@@@@@@@@@@@@@@@           ',
'     %@@@%##@@@@@@@@@@@@@@%           ',
'     #@@%  %%*%***%###@@@@            ',
'     %@@   --==-:::-=+#@@#            ',
'      %%-=++=--==+*++=+#@#            ',
'       *-*#@@*=+%#%*++=%@*=           ',
'       *=*%#@%-=%###%+=%%-+           ',
'       +-+%%%+:=+**+===%*=-           ',
'       +::==+--==---:-=%++-           ',
'       +-.-==:-====::-=%*-:           ',
'       ---=+*==++=+=--=%%:            ',
'       :=+%###%%@%+*=-+@+             ',
'       .++%@@#%%#@@@==%@=             ',
'       .=%%#++*+===**%@@%:            ',
'          %@%=+%%+==+%@@###           ',
'          :#@+-++--=#@@@+#@%          ',
'           -@@#%#%#@@@@-*@@@%+:       ',
'            -%@@@@@@@#--@@@@@@@+:     ',
'              **#@@#%-.@@@@@@@@@@%=   ',
'             =#=****-.+@@@@@@@@@@@@@%+',
'           =%+@%+**-.:@@@@@@@@@@@@@@@@',
'         -#@%-#@+*-..%@@@@@@@@@@@@@@@@',
'       -%@@@+:+@*:::-@@@@@@@@@@@@@@@@@',
'     .*@@@@@=..#+.:-#@@@@@@@@@@@@@@@@@',
'     %@@@@@@%*--=..=@@@@@@@@@@@@@@@@@@',
'     @@@@@@@@@+-:..#@@@@@@@@@@@@@@@@@@'
]

def make_tspans(lines, x, start_y, dy):
    tspans = []
    for i, line in enumerate(lines):
        escaped = html.escape(line).replace(' ', '&#160;')
        tspans.append(f'<tspan x="{x}" y="{start_y + i*dy}">{escaped}</tspan>')
    return '\n    '.join(tspans)

ascii_magenta = make_tspans(raw_lines, 24.3, 64, 11.2)
ascii_cyan = make_tspans(raw_lines, 25.7, 64, 11.2)
ascii_main = make_tspans(raw_lines, 25, 64, 11.2)

# Color squares for palette
palette_colors = ['#484f58', '#ff7b72', '#3fb950', '#d29922', '#58a6ff', '#bc8cff', '#39c5cf', '#f0f6fc']
palette_rects = []
for i, c in enumerate(palette_colors):
    palette_rects.append(f'<rect x="{365 + i * 28}" y="420" width="22" height="13" rx="3" fill="{c}" />')
palette_svg = '\n    '.join(palette_rects)

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 830 465" width="100%" height="100%">
  <defs>
    <style>
      .mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; }}
      .title {{ font-size: 11.5px; fill: #8b949e; font-weight: 500; letter-spacing: 0.3px; }}
      .ascii-glitch-1 {{ font-size: 9.3px; fill: #ff2a6d; opacity: 0.55; }}
      .ascii-glitch-2 {{ font-size: 9.3px; fill: #00f0ff; opacity: 0.55; }}
      .ascii-main {{ font-size: 9.3px; fill: #e6edf3; font-weight: 600; }}
      .neo-header {{ font-size: 14px; font-weight: 700; fill: #58a6ff; letter-spacing: 0.5px; }}
      .neo-sub {{ font-size: 11px; fill: #388bfd; opacity: 0.7; }}
      .lbl {{ font-size: 11.5px; font-weight: 600; }}
      .val {{ font-size: 11.5px; fill: #c9d1d9; }}
      .val-bold {{ font-size: 11.5px; fill: #f0f6fc; font-weight: 600; }}
      .val-accent {{ font-size: 11.5px; fill: #58a6ff; font-weight: 500; }}
    </style>
  </defs>

  <!-- Terminal Window Background -->
  <rect x="0.5" y="0.5" width="829" height="464" rx="12" ry="12" fill="#0b0f14" stroke="#30363d" stroke-width="1.2" />
  
  <!-- Terminal Top Bar -->
  <path d="M 0.5,12 C 0.5,5.5 5.5,0.5 12,0.5 L 818,0.5 C 824.5,0.5 829.5,5.5 829.5,12 L 829.5,35 L 0.5,35 Z" fill="#161b22" stroke="#30363d" stroke-width="1.2" />
  
  <!-- Window Control Buttons -->
  <circle cx="20" cy="18" r="6" fill="#ff5f56" stroke="#e0443e" stroke-width="0.5" />
  <circle cx="38" cy="18" r="6" fill="#ffbd2e" stroke="#dea123" stroke-width="0.5" />
  <circle cx="56" cy="18" r="6" fill="#27c93f" stroke="#1aab29" stroke-width="0.5" />

  <!-- Terminal Title -->
  <text class="mono title" x="415" y="22" text-anchor="middle">aritra@dev: ~/portfolio (zsh)</text>

  <!-- Left: ASCII Portrait (with Cyberpunk Chromatic Aberration) -->
  <text class="mono ascii-glitch-1" xml:space="preserve">
    {ascii_magenta}
  </text>
  <text class="mono ascii-glitch-2" xml:space="preserve">
    {ascii_cyan}
  </text>
  <text class="mono ascii-main" xml:space="preserve">
    {ascii_main}
  </text>

  <!-- Vertical Divider -->
  <line x1="345" y1="46" x2="345" y2="450" stroke="#21262d" stroke-width="1" stroke-dasharray="3 3" />

  <!-- Right: Neofetch Output -->
  <!-- Header -->
  <text class="mono neo-header" x="365" y="66">aritra@iem-kolkata</text>
  <text class="mono neo-sub" x="365" y="80">-------------------------------------------------</text>

  <!-- System Information Rows -->
  <!-- Row 1: OS -->
  <text class="mono lbl" fill="#7ee787" x="365" y="105">OS</text>
  <text class="mono val" x="445" y="105">:: Arch Linux x86_64 / IEM Kolkata</text>

  <!-- Row 2: Education -->
  <text class="mono lbl" fill="#79c0ff" x="365" y="132">Education</text>
  <text class="mono val" x="445" y="132">:: <tspan class="val-bold">B.Tech CSE</tspan> ('27) • <tspan fill="#e3b341">CGPA: 8.55/10</tspan></text>

  <!-- Row 3: Role -->
  <text class="mono lbl" fill="#d2a8ff" x="365" y="159">Role</text>
  <text class="mono val" x="445" y="159">:: Software Engineer &amp; Applied AI / ML</text>

  <!-- Row 4: Research -->
  <text class="mono lbl" fill="#ffa657" x="365" y="186">Research</text>
  <text class="mono val" x="445" y="186">:: <tspan class="val-bold">AI/ML Research Intern @ IIT Patna</tspan></text>
  <text class="mono val" x="462" y="204">(PyTorch, Hyperbolic HMTC, <tspan fill="#56d364">88.57 Micro-F1</tspan>)</text>

  <!-- Row 5: Paper -->
  <text class="mono lbl" fill="#ff7b72" x="365" y="233">Paper</text>
  <text class="mono val" x="445" y="233">:: <tspan class="val-bold">ICDC 2026 Presentation</tspan></text>
  <text class="mono val" x="462" y="251">(Springer Nature proceedings in progress)</text>

  <!-- Row 6: Focus -->
  <text class="mono lbl" fill="#39c5cf" x="365" y="280">Focus</text>
  <text class="mono val" x="445" y="280">:: Resilient Backends • RAG • Multi-Agent</text>

  <!-- Row 7: Core Stack -->
  <text class="mono lbl" fill="#f0883e" x="365" y="307">Stack</text>
  <text class="mono val" x="445" y="307">:: C++, Python, TypeScript, SQL, Node, PyTorch</text>

  <!-- Row 8: Uptime -->
  <text class="mono lbl" fill="#a5d6ff" x="365" y="334">Uptime</text>
  <text class="mono val" x="445" y="334">:: 4th Year Undergrad (Always Shipping)</text>

  <!-- Row 9: Status -->
  <text class="mono lbl" fill="#56d364" x="365" y="361">Status</text>
  <text class="mono val" x="445" y="361">:: <tspan fill="#56d364" font-weight="600">Open to SDE &amp; AI/ML Opportunities</tspan></text>

  <!-- Row 10: Shell / Terminal -->
  <text class="mono lbl" fill="#8b949e" x="365" y="388">Terminal</text>
  <text class="mono val" x="445" y="388">:: zsh 5.9 (tmux + neovim) on kitty</text>

  <!-- Terminal Color Palette Blocks -->
  {palette_svg}

</svg>'''

with open('d:/GitHub readme/terminal.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

print('terminal.svg updated successfully! File size:', len(svg_content))
