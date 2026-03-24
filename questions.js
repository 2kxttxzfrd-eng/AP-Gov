// ============================================================
//  AP U.S. Government & Politics – Question Bank
//  Each question has: id, unit, concept, question, options [A–D],
//  answer (letter), and explanation.
// ============================================================

const QUESTION_BANK = [

  // ─────────────────────────────────────────────
  //  UNIT 1 – Foundations of American Democracy
  // ─────────────────────────────────────────────
  {
    id: 1, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Social Contract Theory",
    question: "Which Enlightenment philosopher argued that people are born with natural rights to life, liberty, and property?",
    options: ["Thomas Hobbes", "John Locke", "Jean-Jacques Rousseau", "Baron de Montesquieu"],
    answer: "B",
    explanation: "John Locke argued that individuals possess natural rights that government must protect."
  },
  {
    id: 2, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Declaration of Independence",
    question: "The Declaration of Independence primarily reflects the ideas of which philosopher?",
    options: ["Montesquieu", "Hobbes", "Locke", "Voltaire"],
    answer: "C",
    explanation: "Jefferson drew heavily on Locke's ideas of natural rights and the social contract."
  },
  {
    id: 3, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Articles of Confederation",
    question: "Which was a major weakness of the Articles of Confederation?",
    options: ["Too much power given to the executive", "Congress could not levy taxes", "The judiciary was too powerful", "States had no sovereignty"],
    answer: "B",
    explanation: "Under the Articles, Congress had no power to tax, making it unable to fund government operations."
  },
  {
    id: 4, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Constitutional Convention",
    question: "The Great Compromise resolved a dispute at the Constitutional Convention about:",
    options: ["Slavery and representation", "Representation in Congress", "Presidential power", "Judicial review"],
    answer: "B",
    explanation: "The Great Compromise created a bicameral legislature with proportional representation in the House and equal representation in the Senate."
  },
  {
    id: 5, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Separation of Powers",
    question: "The idea of separating government into three branches was influenced by:",
    options: ["John Locke", "Montesquieu", "Rousseau", "Voltaire"],
    answer: "B",
    explanation: "Montesquieu's 'The Spirit of the Laws' advocated for separation of powers among legislative, executive, and judicial branches."
  },
  {
    id: 6, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Federalist No. 10",
    question: "In Federalist No. 10, James Madison argues that the best way to control factions is to:",
    options: ["Eliminate all political parties", "Create a large republic", "Give the president veto power", "Establish a bill of rights"],
    answer: "B",
    explanation: "Madison argued a large republic would make it harder for any one faction to dominate."
  },
  {
    id: 7, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Anti-Federalists",
    question: "Anti-Federalists opposed the Constitution primarily because it:",
    options: ["Created a weak national government", "Lacked a bill of rights", "Gave too much power to the states", "Abolished slavery"],
    answer: "B",
    explanation: "Anti-Federalists feared the Constitution gave the federal government too much power without protecting individual liberties."
  },
  {
    id: 8, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Federalist No. 51",
    question: "Federalist No. 51 addresses the need for:",
    options: ["A strong military", "Checks and balances", "Direct democracy", "State sovereignty"],
    answer: "B",
    explanation: "Madison argued in Federalist No. 51 that the structure of government must provide checks and balances to prevent tyranny."
  },
  {
    id: 9, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Republicanism",
    question: "A republican form of government means that:",
    options: ["The people vote directly on all laws", "Elected representatives make decisions for the people", "The president has absolute power", "Only wealthy landowners can vote"],
    answer: "B",
    explanation: "In a republic, citizens elect representatives to make governmental decisions on their behalf."
  },
  {
    id: 10, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Checks and Balances",
    question: "Which is an example of checks and balances?",
    options: ["Congress impeaching the president", "States collecting sales tax", "Citizens voting in elections", "Political parties nominating candidates"],
    answer: "A",
    explanation: "Impeachment is a check by the legislative branch on the executive branch."
  },
  {
    id: 11, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Brutus No. 1",
    question: "Brutus No. 1 warned that a strong national government would:",
    options: ["Protect minority rights", "Threaten individual liberties and state sovereignty", "Promote economic growth", "Strengthen the military"],
    answer: "B",
    explanation: "Brutus No. 1 argued that a large republic with a powerful central government would threaten liberty."
  },
  {
    id: 12, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Three-Fifths Compromise",
    question: "The Three-Fifths Compromise dealt with:",
    options: ["How to elect the president", "How enslaved people would be counted for representation", "The power of the judiciary", "Trade between states"],
    answer: "B",
    explanation: "It counted each enslaved person as three-fifths of a person for apportionment and taxation."
  },

  // ─────────────────────────────────────────────
  //  UNIT 2 – Interactions Among Branches
  // ─────────────────────────────────────────────
  {
    id: 13, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Congressional Powers",
    question: "Which power is exclusive to the House of Representatives?",
    options: ["Ratifying treaties", "Confirming judicial appointments", "Initiating revenue bills", "Trying impeachment cases"],
    answer: "C",
    explanation: "The Constitution requires that all revenue bills originate in the House."
  },
  {
    id: 14, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Senate Powers",
    question: "Which power belongs exclusively to the Senate?",
    options: ["Impeaching federal officials", "Confirming presidential appointments", "Initiating spending bills", "Electing the president if no candidate wins a majority"],
    answer: "B",
    explanation: "The Senate has the power of 'advice and consent' to confirm presidential nominations."
  },
  {
    id: 15, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Presidential Veto",
    question: "Congress can override a presidential veto with:",
    options: ["A simple majority in both chambers", "A two-thirds vote in both chambers", "A three-fourths vote in the Senate", "A unanimous vote in the House"],
    answer: "B",
    explanation: "A two-thirds supermajority in both the House and Senate is required to override a veto."
  },
  {
    id: 16, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Judicial Review",
    question: "The principle of judicial review was established in:",
    options: ["Federalist No. 78", "Marbury v. Madison", "McCulloch v. Maryland", "The Constitution, Article III"],
    answer: "B",
    explanation: "Marbury v. Madison (1803) established the Supreme Court's power to declare laws unconstitutional."
  },
  {
    id: 17, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Formal vs. Informal Powers",
    question: "Which is an informal power of the president?",
    options: ["Vetoing legislation", "Issuing executive orders", "Appointing judges", "Serving as commander in chief"],
    answer: "B",
    explanation: "Executive orders are not explicitly granted in the Constitution but have become accepted presidential practice."
  },
  {
    id: 18, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Bureaucracy",
    question: "Independent regulatory agencies differ from cabinet departments because they:",
    options: ["Are headed by a single secretary", "Can be directly controlled by the president", "Operate outside of presidential control to maintain neutrality", "Are funded by private donations"],
    answer: "C",
    explanation: "Independent regulatory agencies are designed to be insulated from political pressure."
  },
  {
    id: 19, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Congressional Committees",
    question: "Standing committees in Congress are important because they:",
    options: ["Write the final version of all bills", "Conduct most of the detailed work on legislation", "Have the power to override vetoes", "Appoint federal judges"],
    answer: "B",
    explanation: "Standing committees review, revise, and report legislation in their areas of jurisdiction."
  },
  {
    id: 20, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Filibuster",
    question: "A filibuster can be ended by invoking cloture, which requires:",
    options: ["A simple majority", "Two-thirds of the Senate", "Three-fifths (60) senators", "Unanimous consent"],
    answer: "C",
    explanation: "Cloture requires 60 senators to vote to end debate and proceed to a vote."
  },
  {
    id: 21, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "War Powers",
    question: "The War Powers Resolution of 1973 was passed to:",
    options: ["Give the president unlimited military authority", "Limit the president's ability to commit troops without congressional approval", "Abolish the draft", "Create the Department of Defense"],
    answer: "B",
    explanation: "It requires the president to notify Congress within 48 hours and limits deployments to 60 days without authorization."
  },
  {
    id: 22, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Impeachment Process",
    question: "In the impeachment process, the House _____ and the Senate _____.",
    options: ["tries, impeaches", "impeaches, tries", "investigates, impeaches", "votes, investigates"],
    answer: "B",
    explanation: "The House votes to impeach (charge), and the Senate conducts the trial."
  },
  {
    id: 23, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Presidential Appointments",
    question: "Federal judges are appointed by the president and:",
    options: ["Confirmed by the House", "Confirmed by the Senate", "Elected by the people", "Approved by the Supreme Court"],
    answer: "B",
    explanation: "The Senate confirms or rejects presidential nominations to the federal judiciary."
  },
  {
    id: 24, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Bully Pulpit",
    question: "The term 'bully pulpit' refers to the president's ability to:",
    options: ["Bully Congress into passing laws", "Use media access to influence public opinion", "Appoint loyal supporters", "Issue executive orders"],
    answer: "B",
    explanation: "The bully pulpit describes the president's unique platform to shape public discourse."
  },

  // ─────────────────────────────────────────────
  //  UNIT 3 – Civil Liberties and Civil Rights
  // ─────────────────────────────────────────────
  {
    id: 25, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "First Amendment",
    question: "Which right is NOT protected by the First Amendment?",
    options: ["Freedom of speech", "Freedom of the press", "Right to bear arms", "Freedom of religion"],
    answer: "C",
    explanation: "The right to bear arms is protected by the Second Amendment, not the First."
  },
  {
    id: 26, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Selective Incorporation",
    question: "The process by which the Bill of Rights has been applied to the states is called:",
    options: ["Judicial review", "Selective incorporation", "Federalism", "Strict constructionism"],
    answer: "B",
    explanation: "Through the 14th Amendment's Due Process Clause, the Supreme Court has selectively incorporated most Bill of Rights protections to apply to state governments."
  },
  {
    id: 27, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Establishment Clause",
    question: "The Establishment Clause of the First Amendment prohibits:",
    options: ["Individuals from practicing religion", "The government from establishing an official religion", "States from creating their own constitutions", "Congress from declaring war"],
    answer: "B",
    explanation: "The Establishment Clause creates a separation between church and state."
  },
  {
    id: 28, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Free Speech Limitations",
    question: "In Schenck v. United States, the Supreme Court ruled that speech can be limited when it:",
    options: ["Offends public officials", "Creates a 'clear and present danger'", "Is critical of the government", "Is broadcast on television"],
    answer: "B",
    explanation: "Justice Holmes established the 'clear and present danger' test for limiting speech."
  },
  {
    id: 29, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Due Process",
    question: "The 14th Amendment's Due Process Clause has been used to:",
    options: ["Abolish slavery", "Apply the Bill of Rights to the states", "Grant women the right to vote", "Establish the income tax"],
    answer: "B",
    explanation: "The Due Process Clause of the 14th Amendment is the vehicle for selective incorporation."
  },
  {
    id: 30, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Equal Protection",
    question: "The Equal Protection Clause is found in the:",
    options: ["First Amendment", "Fifth Amendment", "Fourteenth Amendment", "Fifteenth Amendment"],
    answer: "C",
    explanation: "The 14th Amendment guarantees equal protection of the laws to all persons."
  },
  {
    id: 31, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Brown v. Board of Education",
    question: "Brown v. Board of Education (1954) ruled that:",
    options: ["Separate but equal is constitutional", "Racial segregation in public schools violates the Equal Protection Clause", "States can set their own education standards", "Affirmative action is constitutional"],
    answer: "B",
    explanation: "The Court overturned Plessy v. Ferguson and declared segregation in public schools unconstitutional."
  },
  {
    id: 32, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Gideon v. Wainwright",
    question: "Gideon v. Wainwright established the right to:",
    options: ["Remain silent", "A speedy trial", "An attorney in felony cases", "Trial by jury"],
    answer: "C",
    explanation: "The Court ruled that states must provide an attorney to defendants who cannot afford one."
  },
  {
    id: 33, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Miranda Rights",
    question: "Miranda v. Arizona requires police to:",
    options: ["Obtain a search warrant before any search", "Inform suspects of their rights before interrogation", "Allow suspects to make a phone call", "Provide suspects with an attorney at arrest"],
    answer: "B",
    explanation: "The Miranda warning ensures suspects know their 5th and 6th Amendment rights."
  },
  {
    id: 34, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Search and Seizure",
    question: "The Fourth Amendment protects against:",
    options: ["Self-incrimination", "Cruel and unusual punishment", "Unreasonable searches and seizures", "Double jeopardy"],
    answer: "C",
    explanation: "The 4th Amendment requires probable cause and generally a warrant for searches."
  },
  {
    id: 35, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Tinker v. Des Moines",
    question: "In Tinker v. Des Moines, the Supreme Court ruled that:",
    options: ["Schools can ban all political expression", "Students retain free speech rights in school", "Students can be expelled for peaceful protest", "Schools must teach political neutrality"],
    answer: "B",
    explanation: "The Court held that students do not 'shed their constitutional rights at the schoolhouse gate.'"
  },
  {
    id: 36, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Civil Rights Act of 1964",
    question: "The Civil Rights Act of 1964 prohibited discrimination based on:",
    options: ["Race, color, religion, sex, and national origin", "Race and gender only", "Age and disability", "Sexual orientation"],
    answer: "A",
    explanation: "The landmark legislation banned discrimination in employment and public accommodations."
  },
  {
    id: 37, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Engel v. Vitale",
    question: "In Engel v. Vitale, the Supreme Court ruled that:",
    options: ["Prayer in public schools is constitutional", "State-sponsored prayer in schools violates the Establishment Clause", "Students cannot pray privately in school", "Schools must offer religious education"],
    answer: "B",
    explanation: "The Court held that government-directed prayer in public schools is unconstitutional."
  },
  {
    id: 38, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "McDonald v. Chicago",
    question: "McDonald v. Chicago incorporated which right to the states?",
    options: ["Freedom of speech", "Right to bear arms", "Right to a jury trial", "Freedom from unreasonable searches"],
    answer: "B",
    explanation: "The Court applied the Second Amendment right to keep and bear arms to state and local governments."
  },

  // ─────────────────────────────────────────────
  //  UNIT 4 – American Political Ideologies and Beliefs
  // ─────────────────────────────────────────────
  {
    id: 39, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Liberal vs. Conservative",
    question: "A liberal political ideology generally favors:",
    options: ["Less government regulation of the economy", "More government involvement in social welfare", "Strict interpretation of the Constitution", "Increased military spending"],
    answer: "B",
    explanation: "Liberals generally support government programs to address social and economic inequality."
  },
  {
    id: 40, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Conservative Ideology",
    question: "A conservative political ideology generally supports:",
    options: ["Expanding social welfare programs", "Limited government and free-market economics", "Increased environmental regulations", "Higher taxes on the wealthy"],
    answer: "B",
    explanation: "Conservatives typically favor limited government, lower taxes, and free-market principles."
  },
  {
    id: 41, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Political Socialization",
    question: "The most significant agent of political socialization is typically:",
    options: ["The media", "Family", "Schools", "Peer groups"],
    answer: "B",
    explanation: "Family is generally the strongest influence on a person's early political beliefs and party identification."
  },
  {
    id: 42, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Public Opinion Polling",
    question: "Which factor is most important for a reliable public opinion poll?",
    options: ["Large sample size", "Random sampling", "Asking leading questions", "Polling only likely voters"],
    answer: "B",
    explanation: "Random sampling ensures every member of the population has an equal chance of being selected."
  },
  {
    id: 43, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Sampling Error",
    question: "The margin of error in a poll indicates:",
    options: ["How biased the poll is", "The range within which the true value likely falls", "The number of people who refused to respond", "How many questions were asked"],
    answer: "B",
    explanation: "Margin of error shows the range of uncertainty in poll results."
  },
  {
    id: 44, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Libertarian Ideology",
    question: "A libertarian generally believes in:",
    options: ["Strong government regulation and social programs", "Minimal government involvement in both economic and social issues", "Government control of the economy but social freedom", "Traditional social values and free-market economics"],
    answer: "B",
    explanation: "Libertarians advocate for maximum individual freedom and minimal government in all areas."
  },
  {
    id: 45, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Political Spectrum",
    question: "On the political spectrum, someone who supports both social welfare programs AND traditional values would be considered:",
    options: ["Liberal", "Conservative", "Libertarian", "Populist"],
    answer: "D",
    explanation: "Populists tend to support government economic intervention while holding traditional social values."
  },
  {
    id: 46, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Media Influence",
    question: "The concept of 'agenda setting' by the media refers to:",
    options: ["The media telling people what to think", "The media influencing what issues people think about", "Politicians controlling news coverage", "Social media replacing traditional news"],
    answer: "B",
    explanation: "Agenda setting is the media's ability to influence the salience of topics on the public agenda."
  },
  {
    id: 47, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Demographic Influences",
    question: "Which demographic group has historically voted most strongly for the Democratic Party?",
    options: ["White evangelical Christians", "Rural voters", "African Americans", "High-income earners"],
    answer: "C",
    explanation: "African Americans have consistently been one of the most loyal Democratic voting blocs."
  },
  {
    id: 48, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Generational Effects",
    question: "A generational effect in political socialization occurs when:",
    options: ["Parents pass on political views to children", "A major event shapes the political views of an entire age cohort", "Schools teach civic education", "Media coverage changes public opinion"],
    answer: "B",
    explanation: "Generational effects occur when shared historical experiences (like 9/11 or the Great Depression) shape an entire generation's political outlook."
  },

  // ─────────────────────────────────────────────
  //  UNIT 5 – Political Participation
  // ─────────────────────────────────────────────
  {
    id: 49, unit: "Unit 5", unitName: "Political Participation",
    concept: "Voter Turnout",
    question: "Voter turnout in the United States is generally:",
    options: ["Higher than most other democracies", "Lower than most other democracies", "About the same as other democracies", "The highest in the world"],
    answer: "B",
    explanation: "The U.S. consistently has lower voter turnout compared to other developed democracies."
  },
  {
    id: 50, unit: "Unit 5", unitName: "Political Participation",
    concept: "Voting Rights",
    question: "The 26th Amendment lowered the voting age to:",
    options: ["16", "18", "19", "21"],
    answer: "B",
    explanation: "Ratified in 1971, the 26th Amendment set the minimum voting age at 18."
  },
  {
    id: 51, unit: "Unit 5", unitName: "Political Participation",
    concept: "Electoral College",
    question: "A candidate needs how many electoral votes to win the presidency?",
    options: ["218", "270", "290", "300"],
    answer: "B",
    explanation: "A majority of 270 out of 538 total electoral votes is needed to win."
  },
  {
    id: 52, unit: "Unit 5", unitName: "Political Participation",
    concept: "Winner-Take-All",
    question: "Most states use a winner-take-all system for electoral votes, which means:",
    options: ["Electoral votes are split proportionally", "The candidate with the most votes gets all the state's electoral votes", "Each congressional district awards one electoral vote", "The popular vote determines the winner"],
    answer: "B",
    explanation: "In 48 states, the candidate who wins the popular vote receives all of that state's electoral votes."
  },
  {
    id: 53, unit: "Unit 5", unitName: "Political Participation",
    concept: "Political Parties",
    question: "The two-party system in the United States is primarily reinforced by:",
    options: ["The Constitution", "Single-member district plurality elections", "Federal campaign finance laws", "The Electoral College alone"],
    answer: "B",
    explanation: "Single-member districts with plurality voting (first-past-the-post) tend to produce two-party systems (Duverger's Law)."
  },
  {
    id: 54, unit: "Unit 5", unitName: "Political Participation",
    concept: "Interest Groups",
    question: "Interest groups primarily try to influence policy by:",
    options: ["Running candidates for office", "Lobbying legislators and government officials", "Organizing voter registration drives", "Filing lawsuits against the government"],
    answer: "B",
    explanation: "Lobbying is the primary method interest groups use to influence policy decisions."
  },
  {
    id: 55, unit: "Unit 5", unitName: "Political Participation",
    concept: "PACs and Super PACs",
    question: "Super PACs differ from traditional PACs because they:",
    options: ["Can donate directly to candidates", "Can raise and spend unlimited money but cannot coordinate with candidates", "Are regulated by the FEC", "Must disclose all donors"],
    answer: "B",
    explanation: "Citizens United v. FEC allowed Super PACs to raise unlimited funds for independent expenditures."
  },
  {
    id: 56, unit: "Unit 5", unitName: "Political Participation",
    concept: "Citizens United v. FEC",
    question: "In Citizens United v. FEC (2010), the Supreme Court ruled that:",
    options: ["Corporations cannot spend money on elections", "Political spending by corporations and unions is protected free speech", "Super PACs must disclose all donors", "Campaign donations must be limited"],
    answer: "B",
    explanation: "The Court held that the First Amendment prohibits limits on independent political expenditures by corporations and unions."
  },
  {
    id: 57, unit: "Unit 5", unitName: "Political Participation",
    concept: "Primary Elections",
    question: "In an open primary:",
    options: ["Only registered party members can vote", "Voters can vote in either party's primary regardless of registration", "All candidates appear on one ballot", "The top two candidates advance"],
    answer: "B",
    explanation: "Open primaries allow voters to choose which party's primary to participate in on election day."
  },
  {
    id: 58, unit: "Unit 5", unitName: "Political Participation",
    concept: "Gerrymandering",
    question: "Gerrymandering is the practice of:",
    options: ["Preventing people from voting", "Drawing district lines to benefit a political party", "Requiring voter identification", "Eliminating the Electoral College"],
    answer: "B",
    explanation: "Gerrymandering manipulates district boundaries to create an advantage for a particular party."
  },
  {
    id: 59, unit: "Unit 5", unitName: "Political Participation",
    concept: "15th Amendment",
    question: "The 15th Amendment prohibits denial of voting rights based on:",
    options: ["Sex", "Age", "Race, color, or previous condition of servitude", "Property ownership"],
    answer: "C",
    explanation: "The 15th Amendment (1870) prohibited racial discrimination in voting."
  },
  {
    id: 60, unit: "Unit 5", unitName: "Political Participation",
    concept: "19th Amendment",
    question: "The 19th Amendment granted voting rights to:",
    options: ["African Americans", "Women", "18-year-olds", "Non-property owners"],
    answer: "B",
    explanation: "Ratified in 1920, the 19th Amendment guaranteed women the right to vote."
  },
  {
    id: 61, unit: "Unit 5", unitName: "Political Participation",
    concept: "Voting Rights Act of 1965",
    question: "The Voting Rights Act of 1965 primarily addressed:",
    options: ["Campaign finance reform", "Eliminating barriers to voting for African Americans", "Lowering the voting age", "Creating the Electoral College"],
    answer: "B",
    explanation: "The Act banned literacy tests and other discriminatory voting practices."
  },
  {
    id: 62, unit: "Unit 5", unitName: "Political Participation",
    concept: "Baker v. Carr",
    question: "Baker v. Carr (1962) established the principle of:",
    options: ["Judicial review", "One person, one vote", "Executive privilege", "Freedom of the press"],
    answer: "B",
    explanation: "The case ruled that redistricting issues are justiciable, leading to the 'one person, one vote' standard."
  },
  {
    id: 63, unit: "Unit 5", unitName: "Political Participation",
    concept: "Shaw v. Reno",
    question: "Shaw v. Reno ruled that redistricting based primarily on race:",
    options: ["Is always constitutional", "Must be reviewed under strict scrutiny", "Is required by the Voting Rights Act", "Is a political question not subject to judicial review"],
    answer: "B",
    explanation: "The Court held that race-based redistricting must be subject to strict scrutiny."
  },

  // ─────────────────────────────────────────────
  //  Additional questions to ensure variety
  // ─────────────────────────────────────────────

  // More Unit 1
  {
    id: 64, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Federalism",
    question: "Federalism is a system in which power is:",
    options: ["Concentrated in a single national government", "Divided between national and state governments", "Held entirely by state governments", "Shared equally among all citizens"],
    answer: "B",
    explanation: "Federalism divides power between a central government and regional (state) governments."
  },
  {
    id: 65, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Supremacy Clause",
    question: "The Supremacy Clause establishes that:",
    options: ["State laws take precedence over federal laws", "The Constitution and federal laws are the supreme law of the land", "The president has supreme power", "The Supreme Court is the highest authority"],
    answer: "B",
    explanation: "Article VI establishes federal law as supreme over conflicting state laws."
  },
  {
    id: 66, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Necessary and Proper Clause",
    question: "The Necessary and Proper Clause (Elastic Clause) gives Congress the power to:",
    options: ["Declare war", "Make laws needed to carry out its enumerated powers", "Override Supreme Court decisions", "Amend the Constitution"],
    answer: "B",
    explanation: "This clause allows Congress flexibility to pass laws beyond those specifically listed in the Constitution."
  },
  {
    id: 67, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "McCulloch v. Maryland",
    question: "McCulloch v. Maryland (1819) established that:",
    options: ["States can tax federal institutions", "The federal government has implied powers and is supreme over states", "The president can veto state laws", "Congress cannot create a national bank"],
    answer: "B",
    explanation: "The Court upheld the Necessary and Proper Clause and ruled that states cannot tax federal institutions."
  },

  // More Unit 2
  {
    id: 68, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Signing Statements",
    question: "A signing statement is used by the president to:",
    options: ["Officially sign a treaty", "Express how they interpret a bill they are signing", "Declare a law unconstitutional", "Request Congress to amend a bill"],
    answer: "B",
    explanation: "Presidents use signing statements to comment on and sometimes challenge provisions of legislation."
  },
  {
    id: 69, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Federal Courts",
    question: "Federal judges serve:",
    options: ["6-year terms", "8-year terms", "Life terms during good behavior", "Until the president removes them"],
    answer: "C",
    explanation: "Article III judges serve life terms to insulate them from political pressure."
  },
  {
    id: 70, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Congressional Oversight",
    question: "Congressional oversight includes all of the following EXCEPT:",
    options: ["Holding committee hearings", "Controlling the federal budget", "Issuing executive orders", "Confirming presidential appointments"],
    answer: "C",
    explanation: "Executive orders are a presidential power, not a tool of congressional oversight."
  },
  {
    id: 71, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Logrolling",
    question: "Logrolling in Congress refers to:",
    options: ["A filibuster strategy", "Trading votes on different bills to gain mutual support", "Adding amendments to kill a bill", "The committee hearing process"],
    answer: "B",
    explanation: "Logrolling is the practice of legislators trading votes to secure passage of their respective bills."
  },
  {
    id: 72, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Pork Barrel Spending",
    question: "Pork barrel spending refers to:",
    options: ["The federal food assistance program", "Government spending on agricultural subsidies", "Directing federal funds to specific projects in a legislator's district", "Emergency disaster relief funding"],
    answer: "C",
    explanation: "Pork barrel spending benefits a specific district to help a member of Congress gain constituent support."
  },

  // More Unit 3
  {
    id: 73, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Roe v. Wade / Dobbs",
    question: "In Dobbs v. Jackson Women's Health Organization (2022), the Supreme Court:",
    options: ["Upheld Roe v. Wade", "Overturned Roe v. Wade, returning abortion policy to the states", "Declared abortion a constitutional right", "Banned all abortions nationwide"],
    answer: "B",
    explanation: "Dobbs overturned Roe, holding that the Constitution does not confer a right to abortion."
  },
  {
    id: 74, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Exclusionary Rule",
    question: "The exclusionary rule prevents:",
    options: ["Defendants from testifying", "Illegally obtained evidence from being used in court", "Judges from making political decisions", "Police from making arrests without warrants"],
    answer: "B",
    explanation: "Established in Mapp v. Ohio, the exclusionary rule bars evidence obtained through illegal searches."
  },
  {
    id: 75, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Cruel and Unusual Punishment",
    question: "The Eighth Amendment prohibits:",
    options: ["Unreasonable searches", "Self-incrimination", "Cruel and unusual punishment", "Double jeopardy"],
    answer: "C",
    explanation: "The 8th Amendment bans excessive bail, excessive fines, and cruel and unusual punishment."
  },
  {
    id: 76, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "New York Times v. United States",
    question: "New York Times v. United States (Pentagon Papers case) established that:",
    options: ["The press can be censored during wartime", "Prior restraint by the government is presumptively unconstitutional", "Newspapers must protect sources", "The government can classify all documents"],
    answer: "B",
    explanation: "The Court ruled against prior restraint, affirming the press's right to publish classified information."
  },
  {
    id: 77, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Wisconsin v. Yoder",
    question: "In Wisconsin v. Yoder, the Supreme Court ruled that:",
    options: ["All children must attend public schools", "Amish families could withdraw children from school after 8th grade based on religious freedom", "Homeschooling is unconstitutional", "States control all education policy"],
    answer: "B",
    explanation: "The Court protected the Amish community's right to limit formal education based on the Free Exercise Clause."
  },

  // More Unit 4
  {
    id: 78, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Party Realignment",
    question: "A critical election that results in a lasting shift in party coalitions is called:",
    options: ["A midterm election", "A realigning election", "A recall election", "A runoff election"],
    answer: "B",
    explanation: "Realigning elections produce long-term changes in party alignment and voter coalitions."
  },
  {
    id: 79, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Gender Gap",
    question: "The 'gender gap' in American politics refers to:",
    options: ["Unequal pay between men and women", "The difference in political views and voting patterns between men and women", "The lack of women in Congress", "Gender-based voter suppression"],
    answer: "B",
    explanation: "Women tend to favor Democratic candidates and support government social programs at higher rates than men."
  },
  {
    id: 80, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Framing",
    question: "When the media presents a story in a particular way to influence interpretation, this is called:",
    options: ["Agenda setting", "Framing", "Priming", "Horse-race journalism"],
    answer: "B",
    explanation: "Framing is how the media packages and presents information, which shapes how audiences interpret it."
  },

  // More Unit 5
  {
    id: 81, unit: "Unit 5", unitName: "Political Participation",
    concept: "Iron Triangles",
    question: "An iron triangle consists of:",
    options: ["The president, Congress, and the Supreme Court", "A congressional committee, a bureaucratic agency, and an interest group", "The House, Senate, and the president", "Federal, state, and local governments"],
    answer: "B",
    explanation: "Iron triangles describe the mutually beneficial relationships between these three entities in policymaking."
  },
  {
    id: 82, unit: "Unit 5", unitName: "Political Participation",
    concept: "Party Platforms",
    question: "A party platform is:",
    options: ["The stage at a political convention", "A set of policy positions adopted by a political party", "The party's fundraising strategy", "A list of candidates running for office"],
    answer: "B",
    explanation: "Party platforms outline the party's positions on key issues and policy goals."
  },
  {
    id: 83, unit: "Unit 5", unitName: "Political Participation",
    concept: "Rational Choice Voting",
    question: "According to rational choice theory, voters:",
    options: ["Always vote based on party loyalty", "Vote for the candidate whose policies will benefit them most", "Make decisions based on emotions", "Follow media recommendations"],
    answer: "B",
    explanation: "Rational choice theory suggests voters weigh costs and benefits to maximize their self-interest."
  },
  {
    id: 84, unit: "Unit 5", unitName: "Political Participation",
    concept: "Retrospective Voting",
    question: "Retrospective voting occurs when voters:",
    options: ["Vote based on a candidate's promises", "Base their decisions on the incumbent's past performance", "Choose candidates based on party affiliation", "Vote based on a candidate's appearance"],
    answer: "B",
    explanation: "Retrospective voters evaluate whether things have gotten better or worse under the current leadership."
  },
  {
    id: 85, unit: "Unit 5", unitName: "Political Participation",
    concept: "Linkage Institutions",
    question: "Which of the following is NOT a linkage institution?",
    options: ["Political parties", "Interest groups", "The bureaucracy", "The media"],
    answer: "C",
    explanation: "The bureaucracy implements policy but does not serve as a link between citizens and government the way parties, interest groups, elections, and media do."
  },
  {
    id: 86, unit: "Unit 5", unitName: "Political Participation",
    concept: "Campaign Finance",
    question: "The Federal Election Commission (FEC) is responsible for:",
    options: ["Running federal elections", "Enforcing campaign finance laws", "Drawing congressional districts", "Counting Electoral College votes"],
    answer: "B",
    explanation: "The FEC administers and enforces federal campaign finance laws."
  },
  {
    id: 87, unit: "Unit 5", unitName: "Political Participation",
    concept: "Third Parties",
    question: "Third parties in the United States most commonly influence politics by:",
    options: ["Winning presidential elections", "Introducing new ideas that major parties eventually adopt", "Controlling Congress", "Appointing federal judges"],
    answer: "B",
    explanation: "Third parties often bring attention to issues that the major parties then incorporate into their platforms."
  },

  // Additional variety questions
  {
    id: 88, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Conference Committee",
    question: "A conference committee is formed to:",
    options: ["Investigate the president", "Reconcile differences between House and Senate versions of a bill", "Oversee federal agencies", "Review Supreme Court nominations"],
    answer: "B",
    explanation: "Conference committees include members from both chambers to produce a compromise version of legislation."
  },
  {
    id: 89, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Power of the Purse",
    question: "The 'power of the purse' belongs to:",
    options: ["The president", "Congress", "The Supreme Court", "The Federal Reserve"],
    answer: "B",
    explanation: "Congress controls federal spending, which serves as a check on the other branches."
  },
  {
    id: 90, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Amendment Process",
    question: "An amendment to the Constitution can be proposed by:",
    options: ["The president", "A two-thirds vote in both houses of Congress or a national convention", "The Supreme Court", "A majority of state governors"],
    answer: "B",
    explanation: "Article V provides two methods: two-thirds of both houses or a convention called by two-thirds of state legislatures."
  },
  {
    id: 91, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Concurrent Powers",
    question: "Concurrent powers are those that:",
    options: ["Belong only to the federal government", "Belong only to state governments", "Are shared by federal and state governments", "Are prohibited to both levels of government"],
    answer: "C",
    explanation: "Examples include the power to tax, build roads, and establish courts."
  },
  {
    id: 92, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "Commerce Clause",
    question: "The Commerce Clause gives Congress the power to:",
    options: ["Coin money", "Regulate interstate and foreign trade", "Declare war", "Establish post offices"],
    answer: "B",
    explanation: "The Commerce Clause has been broadly interpreted to expand federal regulatory power."
  },
  {
    id: 93, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "State of the Union",
    question: "The State of the Union address is an example of the president's role as:",
    options: ["Commander in chief", "Chief legislator", "Head of state", "Chief diplomat"],
    answer: "B",
    explanation: "The president uses the address to propose legislative priorities and set the policy agenda."
  },
  {
    id: 94, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Affirmative Action",
    question: "In Students for Fair Admissions v. Harvard (2023), the Supreme Court ruled that:",
    options: ["Race-conscious admissions programs are constitutional", "Race-conscious admissions programs at colleges violate the Equal Protection Clause", "Affirmative action must be expanded", "Private colleges are exempt from civil rights laws"],
    answer: "B",
    explanation: "The Court struck down race-conscious admissions, effectively ending affirmative action in college admissions."
  },
  {
    id: 95, unit: "Unit 3", unitName: "Civil Liberties and Civil Rights",
    concept: "Letter from Birmingham Jail",
    question: "In his 'Letter from Birmingham Jail,' Martin Luther King Jr. argued that:",
    options: ["Violence is sometimes necessary for justice", "People have a moral obligation to disobey unjust laws", "The federal government should not intervene in state matters", "Court battles are the only way to achieve civil rights"],
    answer: "B",
    explanation: "King defended civil disobedience and the moral duty to oppose unjust laws."
  },
  {
    id: 96, unit: "Unit 4", unitName: "American Political Ideologies and Beliefs",
    concept: "Social Policy",
    question: "Entitlement programs like Social Security and Medicare are difficult to cut because:",
    options: ["They are in the Constitution", "They have broad public support and beneficiaries have paid into them", "The president has veto power over all budget cuts", "They are funded by state governments"],
    answer: "B",
    explanation: "Entitlements are politically difficult to reduce because they affect a large number of voters who feel entitled to benefits."
  },
  {
    id: 97, unit: "Unit 5", unitName: "Political Participation",
    concept: "Voter Registration",
    question: "The Motor Voter Act (1993) made it easier to register to vote by:",
    options: ["Allowing same-day registration", "Allowing registration at DMV offices and other agencies", "Eliminating registration requirements", "Automatically registering all citizens"],
    answer: "B",
    explanation: "The National Voter Registration Act required states to offer voter registration at motor vehicle agencies."
  },
  {
    id: 98, unit: "Unit 5", unitName: "Political Participation",
    concept: "Midterm Elections",
    question: "Midterm elections typically result in:",
    options: ["Higher voter turnout than presidential elections", "The president's party gaining seats", "The president's party losing seats in Congress", "No change in party control"],
    answer: "C",
    explanation: "The president's party historically loses congressional seats during midterm elections."
  },
  {
    id: 99, unit: "Unit 2", unitName: "Interactions Among Branches",
    concept: "Stare Decisis",
    question: "The principle of stare decisis means that courts should:",
    options: ["Always rule in favor of the government", "Follow precedent established by earlier decisions", "Interpret the Constitution literally", "Defer to Congress on all matters"],
    answer: "B",
    explanation: "Stare decisis ('let the decision stand') promotes consistency and predictability in the law."
  },
  {
    id: 100, unit: "Unit 1", unitName: "Foundations of American Democracy",
    concept: "United States v. Lopez",
    question: "In United States v. Lopez (1995), the Supreme Court limited:",
    options: ["The president's executive power", "Congress's use of the Commerce Clause", "The states' power to regulate education", "The judiciary's power of review"],
    answer: "B",
    explanation: "The Court ruled that carrying a gun near a school was not economic activity under the Commerce Clause, limiting federal power."
  }
];
