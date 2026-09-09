import streamlit as st

st.set_page_config(page_title='POLITICAL SCIENCE RESOURCE FINDER', page_icon='🔎', layout='wide', initial_sidebar_state='collapsed')

RESOURCES = [
 ('JSTOR','Scholarly journals, books, and primary sources.','https://www.jstor.org/'),
 ('Google Scholar','Broad scholarly literature discovery across disciplines.','https://scholar.google.com/'),
 ('Scopus','Abstract and citation database for research discovery.','https://www.scopus.com/'),
 ('Web of Science','Citation indexing and multidisciplinary literature discovery.','https://www.webofscience.com/'),
 ('EBSCOhost','Research databases with extensive social-science coverage.','https://www.ebsco.com/'),
 ('ProQuest','Dissertations, theses, journals, and research databases.','https://www.proquest.com/'),
 ('TheSoz','GESIS thesaurus for social-science terminology.','https://www.gesis.org/en/services/tools/the-sos'),
 ('ELSST','CESSDA multilingual social-science thesaurus.','https://elsst.cessda.eu/'),
 ('DOAJ','Open-access journals across scholarly disciplines.','https://doaj.org/'),
 ('Crossref','Scholarly metadata and DOI discovery.','https://search.crossref.org/'),
 ('CORE','Large-scale open-access research discovery.','https://core.ac.uk/'),
 ('OpenAlex','Open scholarly metadata for works, authors, and sources.','https://openalex.org/'),
 ('Semantic Scholar','AI-assisted scholarly literature discovery.','https://www.semanticscholar.org/'),
 ('Project MUSE','Humanities and social-science journals and books.','https://muse.jhu.edu/'),
 ('HeinOnline','Academic journals, government, and international resources.','https://heinonline.org/'),
 ('ICPSR','Social-science data archive and research datasets.','https://www.icpsr.umich.edu/'),
 ('APSA','Political science journals, publications, and resources.','https://apsanet.org/'),
 ('IPSA Portal','Curated political-science web resources.','https://www.ipsa.org/resources/ipsaportal'),
 ('ECPR','European political-science research and publishing resources.','https://ecpr.eu/'),
 ('Cambridge Core','Political science and international-relations scholarship.','https://www.cambridge.org/core/browse-subjects/politics-and-international-relations'),
 ('Oxford Academic','Political science and political methodology journals.','https://academic.oup.com/'),
 ('Elsevier','Publisher platform with social and political research journals.','https://www.elsevier.com/en-in/subject/social-sciences/journals'),
 ('SAGE Publishing','Major social-science and political-science journal publisher.','https://journals.sagepub.com/'),
 ('ResearchGate','Research network and publication discovery platform.','https://www.researchgate.net/'),
]

EXAMPLES = {
 'PICO': {'Population':'Indian university students','Intervention':'Digital political participation','Comparison':'Traditional political participation','Outcome':'Political engagement'},
 'PECO': {'Population':'Young adults','Exposure':'Social media political content','Comparator':'Low social-media exposure','Outcome':'Political participation'},
 'SPIDER': {'Sample':'First-time voters','Phenomenon of Interest':'Online political mobilisation','Design':'Qualitative interviews','Evaluation':'Political attitudes','Research type':'Qualitative'},
 'PCC': {'Population':'Religious minorities','Concept':'Political representation','Context':'Contemporary India'}
}
FIELDS = {
 'PICO':['Population','Intervention','Comparison','Outcome'],
 'PECO':['Population','Exposure','Comparator','Outcome'],
 'SPIDER':['Sample','Phenomenon of Interest','Design','Evaluation','Research type'],
 'PCC':['Population','Concept','Context']
}

st.markdown('''<style>
#MainMenu,footer,header{visibility:hidden} .stApp{background:#f7f8fa;color:#172033} .block-container{max-width:1180px;padding:0 28px 40px}
.top{height:62px;background:#102a43;color:white;display:flex;align-items:center;justify-content:center;margin:0 -28px;padding:0 20px}.top h1{font-size:18px;letter-spacing:.04em;margin:0;font-weight:750}
.nav{height:43px;background:#183b5b;margin:0 -28px 34px;display:flex;align-items:center;justify-content:center;gap:8px;overflow-x:auto}.nav a{color:#dbe8f3;text-decoration:none;font-size:12px;padding:8px 13px;border-radius:7px}.nav a:hover{background:#244e70}
.hero{text-align:center;padding:16vh 0 10vh}.hero h2{font-size:30px;letter-spacing:.03em;margin-bottom:10px}.hero p{font-size:14px;color:#617083}.search{max-width:760px;margin:auto}
.card{background:white;border:1px solid #dfe5eb;border-radius:12px;padding:20px;min-height:150px;box-shadow:0 2px 8px rgba(20,40,60,.04)}.card h3{font-size:16px;margin:8px 0}.card p{font-size:13px;color:#637083;line-height:1.45}.eyebrow{font-size:11px;font-weight:700;letter-spacing:.12em;color:#58718a;text-align:center}.pagehead{text-align:center;margin:18px 0 28px}.pagehead h2{font-size:23px;letter-spacing:.04em}.pagehead p{font-size:13px;color:#667587}
.section{margin-top:25px}.question{background:white;border:1px solid #dfe5eb;border-radius:12px;padding:20px;font-size:15px;line-height:1.6}.small{font-size:12px;color:#6a7786}
@media(max-width:700px){.block-container{padding:0 12px 28px}.top{margin:0 -12px;height:56px}.top h1{font-size:13px}.nav{margin:0 -12px 24px;height:42px;gap:0;justify-content:space-between}.nav a{font-size:9px;padding:7px 6px;flex:1;text-align:center}.hero{padding:16vh 0 10vh}.hero h2{font-size:22px}.card{min-height:0}.pagehead h2{font-size:19px}}
</style>''', unsafe_allow_html=True)

st.markdown('<div class="top"><h1>POLITICAL SCIENCE RESOURCE FINDER</h1></div>',unsafe_allow_html=True)
nav=st.radio('Navigation',['HOME','RESOURCES','CONCEPTS','FRAMEWORK','STRATEGY'],horizontal=True,label_visibility='collapsed')

if nav=='HOME':
 st.markdown('<div class="hero"><h2>FIND THE RIGHT SCHOLARLY RESOURCES</h2><p>Search databases, thesauri, and scholarly research platforms.</p></div>',unsafe_allow_html=True)
 q=st.text_input('Search',placeholder='Search resources, databases, thesauri, publishers…',label_visibility='collapsed')
 if q:
  matches=[r for r in RESOURCES if q.lower() in ' '.join(r[:2]).lower()]
  st.markdown(f'**{len(matches)} matching resources**')
  cols=st.columns(3)
  for i,(n,d,u) in enumerate(matches):
   with cols[i%3]: st.markdown(f'<div class="card"><h3>{n}</h3><p>{d}</p><a href="{u}" target="_blank">OPEN RESOURCE →</a></div>',unsafe_allow_html=True)

elif nav=='RESOURCES':
 st.markdown('<div class="pagehead"><h2>POLITICAL SCIENCE RESOURCE DIRECTORY</h2><p>Curated scholarly resources for political-science research.</p></div>',unsafe_allow_html=True)
 q=st.text_input('Filter resources',placeholder='Filter the directory…',label_visibility='collapsed')
 items=[r for r in RESOURCES if not q or q.lower() in ' '.join(r[:2]).lower()]
 cols=st.columns(3)
 for i,(n,d,u) in enumerate(items):
  with cols[i%3]: st.markdown(f'<div class="card"><h3>{n}</h3><p>{d}</p><a href="{u}" target="_blank">OPEN RESOURCE →</a></div>',unsafe_allow_html=True)

elif nav=='CONCEPTS':
 st.markdown('<div class="pagehead"><h2>CONCEPT MAPPER</h2><p>Expand research concepts into usable search terms.</p></div>',unsafe_allow_html=True)
 raw=st.text_area('Concepts',placeholder='Enter concepts, one per line or separated by commas…',height=140,label_visibility='collapsed')
 terms=[x.strip() for x in raw.replace(',','\n').splitlines() if x.strip()]
 if terms:
  for t in terms: st.markdown(f'**{t.upper()}**  →  {t} OR "{t}"')
 else: st.info('Enter concepts to begin mapping.')

elif nav=='FRAMEWORK':
 st.markdown('<div class="pagehead"><h2>STRUCTURE YOUR RESEARCH QUESTION</h2><p>Choose a framework, add terms and synonyms, and build your research question.</p></div>',unsafe_allow_html=True)
 fw=st.radio('Framework',['PICO','PECO','SPIDER','PCC'],horizontal=True)
 if 'fwvals' not in st.session_state or st.session_state.get('lastfw')!=fw:
  st.session_state.fwvals=EXAMPLES[fw].copy() if False else {k:'' for k in FIELDS[fw]}; st.session_state.lastfw=fw
 c1,c2=st.columns(2)
 for i,k in enumerate(FIELDS[fw]):
  with (c1 if i%2==0 else c2): st.session_state.fwvals[k]=st.text_input(k,value=st.session_state.fwvals[k],key=f'{fw}_{k}')
 a=st.columns(2)
 if a[0].button('LOAD EXAMPLE'):
  for k,v in EXAMPLES[fw].items(): st.session_state.fwvals[k]=v
  st.rerun()
 if a[1].button('CLEAR'):
  for k in FIELDS[fw]: st.session_state.fwvals[k]=''
  st.rerun()
 vals=[v for v in st.session_state.fwvals.values() if v]
 if vals:
  st.markdown('<div class="section"><div class="eyebrow">STRUCTURED RESEARCH QUESTION</div></div>',unsafe_allow_html=True)
  st.markdown('<div class="question">'+'; '.join(vals)+'.</div>',unsafe_allow_html=True)

else:
 st.markdown('<div class="pagehead"><h2>SEARCH STRATEGY BUILDER</h2><p>Construct transparent Boolean search logic from your concepts.</p></div>',unsafe_allow_html=True)
 raw=st.text_area('Search concepts',placeholder='Enter concepts, one per line or separated by commas…',height=140,label_visibility='collapsed')
 db=st.multiselect('Database targets',['JSTOR','Scopus','Web of Science','EBSCOhost','ProQuest','Google Scholar'],default=['Google Scholar'])
 terms=[x.strip() for x in raw.replace(',','\n').splitlines() if x.strip()]
 if terms:
  boolean=' AND '.join(f'({t} OR "{t}")' for t in terms)
  st.code(boolean)
  st.caption('OR joins synonyms within a concept; AND joins concepts.')

st.markdown('<p class="small" style="text-align:center;margin-top:50px">POLITICAL SCIENCE RESOURCE FINDER · ACADEMIC RESEARCH TOOL</p>',unsafe_allow_html=True)
