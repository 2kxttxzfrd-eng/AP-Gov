#!/usr/bin/env python3
"""
Generate question_bank.py with 500 AP Gov questions.
Balanced answer distribution (~125 A, 125 B, 125 C, 125 D).
Includes stimulus-based questions.
Correct answer is NOT always the longest option.
"""

import json, textwrap

# Each tuple: (unit, unitName, concept, question, options_list, correct_index_0based, explanation)
# correct_index: 0=A, 1=B, 2=C, 3=D

RAW = [
    # ══════════════════════════════════════════════════════════════
    #  UNIT 1 — Foundations of American Democracy (100 questions)
    # ══════════════════════════════════════════════════════════════

    ("Unit 1","Foundations of American Democracy","Social Contract Theory",
     "Which Enlightenment philosopher argued that people are born with natural rights to life, liberty, and property?",
     ["John Locke","Thomas Hobbes","Jean-Jacques Rousseau","Baron de Montesquieu"],0,
     "John Locke argued that individuals possess natural rights that government must protect."),

    ("Unit 1","Foundations of American Democracy","Declaration of Independence",
     "The Declaration of Independence primarily reflects the ideas of which philosopher?",
     ["Montesquieu","Hobbes","Voltaire","John Locke"],3,
     "Jefferson drew heavily on Locke's ideas of natural rights and the social contract."),

    ("Unit 1","Foundations of American Democracy","Articles of Confederation",
     "Which was a major weakness of the Articles of Confederation?",
     ["Too much executive power","The judiciary was too powerful","Congress could not levy taxes","States had no sovereignty"],2,
     "Under the Articles, Congress had no power to tax, making it unable to fund government operations."),

    ("Unit 1","Foundations of American Democracy","Constitutional Convention",
     "The Great Compromise resolved a dispute at the Constitutional Convention about:",
     ["Representation in Congress","Slavery","Presidential power","Judicial review"],0,
     "The Great Compromise created a bicameral legislature with proportional and equal representation."),

    ("Unit 1","Foundations of American Democracy","Separation of Powers",
     "The idea of separating government into three branches was most directly influenced by:",
     ["John Locke","Rousseau","Voltaire","Montesquieu"],3,
     "Montesquieu advocated for separation of powers among legislative, executive, and judicial branches."),

    ("Unit 1","Foundations of American Democracy","Federalist No. 10",
     "In Federalist No. 10, James Madison argues that the best way to control factions is to:",
     ["Eliminate all political parties","Give the president veto power","Create a large republic","Establish a bill of rights"],2,
     "Madison argued a large republic would make it harder for any one faction to dominate."),

    ("Unit 1","Foundations of American Democracy","Anti-Federalists",
     "Anti-Federalists opposed ratification primarily because the Constitution:",
     ["Lacked a bill of rights","Created a weak government","Gave too much power to the states","Abolished slavery"],0,
     "Anti-Federalists feared the federal government had too much power without protecting individual liberties."),

    ("Unit 1","Foundations of American Democracy","Federalist No. 51",
     "Federalist No. 51 addresses the need for:",
     ["A strong military","Direct democracy","State sovereignty","Checks and balances"],3,
     "Madison argued that government structure must provide checks and balances to prevent tyranny."),

    ("Unit 1","Foundations of American Democracy","Republicanism",
     "A republican form of government means that:",
     ["The people vote directly on all laws","Only landowners can vote","The president has absolute power","Elected representatives make decisions for the people"],3,
     "In a republic, citizens elect representatives to make governmental decisions on their behalf."),

    ("Unit 1","Foundations of American Democracy","Checks and Balances",
     "Which is an example of checks and balances?",
     ["The Senate approving a state law","A governor signing a treaty","The president vetoing a bill passed by Congress","States amending the Constitution alone"],2,
     "The presidential veto is a check on legislative power."),

    ("Unit 1","Foundations of American Democracy","Necessary and Proper Clause",
     "The Necessary and Proper Clause gives Congress the power to:",
     ["Declare war only","Amend the Constitution","Override the Supreme Court","Pass laws needed to carry out its enumerated powers"],3,
     "Also called the Elastic Clause, it allows Congress flexibility to carry out its duties."),

    ("Unit 1","Foundations of American Democracy","Supremacy Clause",
     "The Supremacy Clause establishes that:",
     ["Federal law is the supreme law of the land","States can override federal law","The president is above the law","The Supreme Court has final say on all matters"],0,
     "Article VI makes federal law supreme over conflicting state laws."),

    ("Unit 1","Foundations of American Democracy","Federalism",
     "Federalism is a system of government in which power is:",
     ["Concentrated in the national government","Held only by state governments","Shared between national and state governments","Exercised by the judiciary alone"],2,
     "Federalism divides power between national and state levels."),

    ("Unit 1","Foundations of American Democracy","Enumerated Powers",
     "Which is an enumerated power of Congress?",
     ["Establishing local police departments","Setting speed limits on highways","Regulating interstate commerce","Issuing driver's licenses"],2,
     "The power to regulate interstate commerce is explicitly listed in Article I, Section 8."),

    ("Unit 1","Foundations of American Democracy","Reserved Powers",
     "Under the Tenth Amendment, powers not delegated to the federal government are:",
     ["Abolished","Reserved to the states or the people","Given to the president","Held by the judiciary"],1,
     "The Tenth Amendment reserves undelegated powers to states or the people."),

    ("Unit 1","Foundations of American Democracy","Concurrent Powers",
     "Which is a concurrent power shared by both federal and state governments?",
     ["The power to tax","The power to coin money","The power to declare war","The power to conduct foreign affairs"],0,
     "Both levels of government can levy taxes."),

    ("Unit 1","Foundations of American Democracy","Full Faith and Credit Clause",
     "The Full Faith and Credit Clause requires that:",
     ["States must honor the public acts and records of other states","Federal courts must hear all state cases","Citizens pay taxes in every state they visit","States must adopt identical laws"],0,
     "Article IV requires states to recognize the legal proceedings of other states."),

    ("Unit 1","Foundations of American Democracy","Commerce Clause",
     "The Commerce Clause has been used primarily to:",
     ["Limit the president's power","Reduce the federal budget","Expand federal regulatory authority","Eliminate state governments"],2,
     "The Commerce Clause has been interpreted broadly to expand Congress's regulatory power."),

    ("Unit 1","Foundations of American Democracy","Brutus No. 1",
     "Brutus No. 1 warned that the proposed Constitution would:",
     ["Protect individual liberties effectively","Create a government too weak to function","Lead to the destruction of state sovereignty","Strengthen the Articles of Confederation"],2,
     "The Anti-Federalist essay argued the new government would absorb state power."),

    ("Unit 1","Foundations of American Democracy","Amendment Process",
     "An amendment to the Constitution can be proposed by:",
     ["The president alone","A two-thirds vote in both houses of Congress","A simple majority in the House","The Supreme Court"],1,
     "Article V requires a two-thirds vote in both chambers or a constitutional convention called by the states."),

    # Stimulus-based Q
    ("Unit 1","Foundations of American Democracy","Federalist No. 10 (Stimulus)",
     "\"The latent causes of faction are thus sown in the nature of man.\" — James Madison, Federalist No. 10\n\nBased on the quote, Madison believed that factions:",
     ["Can be eliminated through education","Are an inevitable part of human nature","Should be outlawed by the government","Only arise in small republics"],1,
     "Madison acknowledged factions are natural and focused on controlling their effects rather than eliminating them."),

    ("Unit 1","Foundations of American Democracy","Federalist No. 51 (Stimulus)",
     "\"If men were angels, no government would be necessary.\" — James Madison, Federalist No. 51\n\nThis quote supports the argument that:",
     ["Democracy is impossible","People are inherently good","Government must have mechanisms to control itself and those it governs","The Articles of Confederation were sufficient"],2,
     "Madison argued that because people are not perfect, government with checks is essential."),

    ("Unit 1","Foundations of American Democracy","Constitutional Principles",
     "Popular sovereignty means that:",
     ["Government power comes from the people","The president has supreme authority","States are sovereign over the federal government","Judges make all final decisions"],0,
     "Popular sovereignty holds that legitimate government authority derives from the consent of the governed."),

    ("Unit 1","Foundations of American Democracy","Three-Fifths Compromise",
     "The Three-Fifths Compromise addressed the issue of:",
     ["Presidential elections","Judicial appointments","How enslaved people would be counted for representation and taxation","Freedom of speech"],2,
     "Enslaved people were counted as three-fifths of a person for apportionment and taxation."),

    ("Unit 1","Foundations of American Democracy","Ratification Debate",
     "The Federalist Papers were written primarily to:",
     ["Oppose the Constitution","Persuade New York to ratify the Constitution","Amend the Articles of Confederation","Establish the Bill of Rights"],1,
     "Hamilton, Madison, and Jay wrote the Federalist Papers to build support for ratification."),

    ("Unit 1","Foundations of American Democracy","Limited Government",
     "The concept of limited government means that:",
     ["Government power is restricted by law","The government can do anything it wants","Only the judiciary has limits","States have no power"],0,
     "Limited government means officials must operate within constitutional constraints."),

    ("Unit 1","Foundations of American Democracy","Natural Rights",
     "According to John Locke, if a government violates the social contract, people have the right to:",
     ["Obey without question","Alter or abolish the government","Appeal to a foreign power","Ignore all laws permanently"],1,
     "Locke argued the people can replace a government that fails to protect their rights."),

    ("Unit 1","Foundations of American Democracy","Participatory Democracy",
     "Participatory democracy emphasizes:",
     ["Elite decision-making","Broad citizen involvement in politics","Military rule","Judicial supremacy"],1,
     "Participatory democracy values direct citizen engagement in political processes."),

    ("Unit 1","Foundations of American Democracy","Pluralist Democracy",
     "A pluralist model of democracy holds that:",
     ["One elite group controls policy","Power is spread among many competing groups","Only wealthy people have influence","The president decides everything"],1,
     "Pluralism asserts that policy emerges from competition among diverse interest groups."),

    ("Unit 1","Foundations of American Democracy","Elite Democracy",
     "The elitist theory of democracy argues that:",
     ["All citizens have equal power","A small number of wealthy and powerful individuals dominate politics","Interest groups don't matter","Congress represents everyone equally"],1,
     "Elite theory holds that a small, powerful group disproportionately influences government."),

    ("Unit 1","Foundations of American Democracy","Marbury v. Madison",
     "Marbury v. Madison (1803) established the principle of:",
     ["Judicial review","Executive privilege","Federalism","Popular sovereignty"],0,
     "Chief Justice Marshall's ruling established the Supreme Court's power to strike down unconstitutional laws."),

    ("Unit 1","Foundations of American Democracy","McCulloch v. Maryland",
     "In McCulloch v. Maryland (1819), the Supreme Court ruled that:",
     ["States cannot tax federal institutions","The president can dissolve Congress","The Bill of Rights does not apply to states","Congress cannot establish a national bank"],0,
     "The Court upheld the national bank and ruled states cannot tax the federal government."),

    ("Unit 1","Foundations of American Democracy","United States v. Lopez",
     "In United States v. Lopez (1995), the Supreme Court limited:",
     ["The president's executive power","The states' power to regulate education","The judiciary's power of review","Congress's use of the Commerce Clause"],3,
     "The Court ruled that carrying a gun near a school was not economic activity under the Commerce Clause."),

    ("Unit 1","Foundations of American Democracy","Implied Powers",
     "Implied powers of Congress are those that are:",
     ["Explicitly listed in Article I","Not in the Constitution but necessary to carry out enumerated powers","Reserved to the states","Granted by the president"],1,
     "Implied powers derive from the Necessary and Proper Clause."),

    ("Unit 1","Foundations of American Democracy","Cooperative Federalism",
     "Cooperative federalism is best described as:",
     ["States acting completely independently","Federal and state governments sharing responsibilities on policy issues","The federal government controlling everything","States ignoring federal mandates"],1,
     "Cooperative federalism involves intergovernmental collaboration on programs."),

    ("Unit 1","Foundations of American Democracy","Dual Federalism",
     "Dual federalism is often compared to a:",
     ["Marble cake","Layer cake","Pie chart","Spider web"],1,
     "Dual federalism, or 'layer cake' federalism, features clearly separated federal and state responsibilities."),

    ("Unit 1","Foundations of American Democracy","Block Grants",
     "Block grants give state governments:",
     ["No federal money","Broad discretion in how to spend federal funds","Money only for education","Funds that must be returned to the federal government"],1,
     "Block grants provide federal funds with general guidelines, giving states flexibility."),

    ("Unit 1","Foundations of American Democracy","Categorical Grants",
     "Categorical grants differ from block grants because they:",
     ["Have strict federal guidelines on how money must be spent","Give states total freedom","Are never used anymore","Only go to local governments"],0,
     "Categorical grants come with specific conditions and requirements."),

    ("Unit 1","Foundations of American Democracy","Unfunded Mandates",
     "Unfunded mandates require state governments to:",
     ["Give money to the federal government","Comply with federal regulations without receiving federal funding","Ignore federal law","Eliminate their legislatures"],1,
     "States must implement federal requirements but do not receive funds to do so."),

    ("Unit 1","Foundations of American Democracy","Selective Incorporation",
     "Selective incorporation applies the Bill of Rights to the states through the:",
     ["Supremacy Clause","Commerce Clause","Fourteenth Amendment's Due Process Clause","Tenth Amendment"],2,
     "The Supreme Court has used the 14th Amendment to apply individual protections to states case by case."),

    # Stimulus
    ("Unit 1","Foundations of American Democracy","Brutus No. 1 (Stimulus)",
     "\"In a republic of such vast extent...the legislature...would be composed of such heterogeneous and discordant principles, as would constantly be contending with each other.\" — Brutus No. 1\n\nThe author's main concern is that:",
     ["A large republic will have too many conflicting interests to function effectively","Small republics are unstable","The judiciary will become too powerful","Factions can be easily controlled"],0,
     "Brutus worried that a large, diverse republic would be ungovernable."),

    ("Unit 1","Foundations of American Democracy","Fiscal Federalism (Stimulus)",
     "A state receives a federal grant requiring that 80% of funds be used for highway repair and 20% for bridge maintenance. This is an example of:",
     ["A block grant","An unfunded mandate","A categorical grant","Revenue sharing"],2,
     "The specific spending requirements make this a categorical grant."),

    ("Unit 1","Foundations of American Democracy","Devolution",
     "Devolution refers to:",
     ["Increasing federal power over the states","Transferring power from the federal government to state and local governments","Eliminating state governments","Combining the legislative and executive branches"],1,
     "Devolution shifts responsibilities and authority from Washington to the states."),

    ("Unit 1","Foundations of American Democracy","Privileges and Immunities Clause",
     "The Privileges and Immunities Clause prevents states from:",
     ["Discriminating against citizens of other states in fundamental rights","Passing any laws","Collecting sales tax from visitors","Holding elections"],0,
     "States cannot deny fundamental rights to out-of-state citizens."),

    ("Unit 1","Foundations of American Democracy","Article V",
     "What fraction of state legislatures must ratify a proposed amendment?",
     ["One-half","Two-thirds","Three-fourths","Four-fifths"],2,
     "Three-fourths (38 of 50) of state legislatures must ratify an amendment."),

    ("Unit 1","Foundations of American Democracy","Hobbes vs. Locke",
     "Thomas Hobbes and John Locke agreed that:",
     ["Government should be a monarchy","People form governments through a social contract","Revolution is always justified","Rights are not natural"],1,
     "Both believed in the social contract, though they disagreed on government's nature."),

    ("Unit 1","Foundations of American Democracy","Electoral College Origins",
     "The Framers created the Electoral College because they:",
     ["Trusted direct democracy fully","Wanted to balance popular will with elite judgment","Opposed any form of elections","Believed only senators should choose the president"],1,
     "The Electoral College was a compromise between direct popular vote and congressional selection."),

    ("Unit 1","Foundations of American Democracy","Elastic Clause Application",
     "Congress used the Necessary and Proper Clause to justify creating:",
     ["The National Park System only","The Department of Defense only","A national bank and many federal agencies","State legislatures"],2,
     "The Elastic Clause has been used to create institutions like the national bank and federal agencies."),

    # ══════════════════════════════════════════════════════════════
    #  UNIT 2 — Interactions Among Branches of Government (100 qs)
    # ══════════════════════════════════════════════════════════════

    ("Unit 2","Interactions Among Branches","Congressional Powers",
     "Which is an expressed power of Congress?",
     ["Establishing public schools","Regulating local zoning","Declaring war","Issuing driver's licenses"],2,
     "The power to declare war is explicitly granted to Congress in Article I."),

    ("Unit 2","Interactions Among Branches","Impeachment",
     "The power to impeach a federal official belongs to:",
     ["The House of Representatives","The Senate","The Supreme Court","The president"],0,
     "The House has the sole power of impeachment; the Senate conducts the trial."),

    ("Unit 2","Interactions Among Branches","Senate Confirmation",
     "The Senate must confirm presidential appointments to:",
     ["State legislatures","Local school boards","Federal courts and cabinet positions","City councils"],2,
     "Advice and consent power gives the Senate a role in confirming federal judges and cabinet members."),

    ("Unit 2","Interactions Among Branches","Filibuster",
     "A filibuster in the Senate can be ended by:",
     ["A simple majority vote","A presidential order","The Speaker of the House","A cloture vote of 60 senators"],3,
     "Cloture requires 60 votes to end debate and force a vote on legislation."),

    ("Unit 2","Interactions Among Branches","Speaker of the House",
     "The Speaker of the House is significant because they:",
     ["Are appointed by the president","Control the legislative agenda and floor proceedings","Serve as head of the judiciary","Can override presidential vetoes alone"],1,
     "The Speaker controls which bills come to the floor and influences the legislative process."),

    ("Unit 2","Interactions Among Branches","Committee System",
     "Standing committees in Congress are important because they:",
     ["Write the final version of all laws","Have no real power","Review and shape legislation before it reaches the full chamber","Only deal with foreign policy"],2,
     "Standing committees specialize in policy areas and do the detailed work on legislation."),

    ("Unit 2","Interactions Among Branches","Conference Committee",
     "A conference committee is formed when:",
     ["The president requests it","The Supreme Court orders it","The House and Senate pass different versions of the same bill","A bill is vetoed"],2,
     "Conference committees reconcile differences between House and Senate versions of legislation."),

    ("Unit 2","Interactions Among Branches","Presidential Veto",
     "The president can check congressional power by:",
     ["Dissolving Congress","Vetoing legislation","Appointing new members of Congress","Changing the Constitution"],1,
     "The veto allows the president to reject bills, requiring a two-thirds override vote."),

    ("Unit 2","Interactions Among Branches","Veto Override",
     "Congress can override a presidential veto with:",
     ["A simple majority in one chamber","A two-thirds vote in both chambers","A unanimous vote in the Senate","Approval from the Supreme Court"],1,
     "A two-thirds supermajority in both the House and Senate overrides a veto."),

    ("Unit 2","Interactions Among Branches","Executive Orders",
     "Executive orders allow the president to:",
     ["Create new laws without Congress","Direct federal agencies on policy implementation","Amend the Constitution","Remove Supreme Court justices"],1,
     "Executive orders direct how executive agencies implement policy within existing law."),

    ("Unit 2","Interactions Among Branches","War Powers Resolution",
     "The War Powers Resolution of 1973 requires the president to:",
     ["Seek congressional approval to declare war","Notify Congress within 48 hours of deploying troops","Get Supreme Court approval before military action","Consult with the United Nations first"],1,
     "The president must notify Congress within 48 hours and withdraw troops within 60 days without authorization."),

    ("Unit 2","Interactions Among Branches","Judicial Review",
     "Judicial review gives the Supreme Court the power to:",
     ["Write new legislation","Override executive orders automatically","Declare laws unconstitutional","Appoint new judges"],2,
     "Judicial review allows courts to strike down laws that violate the Constitution."),

    ("Unit 2","Interactions Among Branches","Stare Decisis",
     "The principle of stare decisis means that courts should:",
     ["Follow precedent established by earlier decisions","Always side with the government","Interpret the Constitution literally","Defer to Congress on everything"],0,
     "Stare decisis promotes consistency by following previous judicial rulings."),

    ("Unit 2","Interactions Among Branches","Appointment Power",
     "The president nominates federal judges who must be confirmed by:",
     ["The House of Representatives","State governors","A national referendum","The Senate"],3,
     "The Senate provides advice and consent on judicial nominations."),

    ("Unit 2","Interactions Among Branches","Bureaucratic Discretion",
     "Bureaucratic discretion refers to the ability of agencies to:",
     ["Ignore all laws","Make judgments in implementing policy within guidelines Congress sets","Override the president","Amend the Constitution"],1,
     "Agencies use discretion to interpret and apply broadly written statutes."),

    ("Unit 2","Interactions Among Branches","Iron Triangles",
     "An iron triangle consists of:",
     ["The president, vice president, and Speaker","A congressional committee, an interest group, and a bureaucratic agency","Three branches of government","Three political parties"],1,
     "Iron triangles are mutually beneficial relationships among committees, agencies, and interest groups."),

    ("Unit 2","Interactions Among Branches","Presidential Persuasion",
     "Richard Neustadt argued that presidential power is primarily the power to:",
     ["Command the military","Persuade others to act","Veto legislation","Appoint judges"],1,
     "Neustadt emphasized that presidents succeed through bargaining and persuasion, not just formal authority."),

    ("Unit 2","Interactions Among Branches","Bully Pulpit",
     "The 'bully pulpit' refers to the president's ability to:",
     ["Use the military to enforce laws","Use the visibility of the office to shape public opinion","Override Congress","Appoint favorable judges"],1,
     "Presidents leverage media attention and public speaking to build support for their agenda."),

    ("Unit 2","Interactions Among Branches","Signing Statements",
     "Presidential signing statements are used to:",
     ["Veto parts of a bill","Express the president's interpretation of a law when signing it","Override the Supreme Court","Create new legislation"],1,
     "Presidents use signing statements to indicate how they intend to enforce or interpret legislation."),

    ("Unit 2","Interactions Among Branches","Power of the Purse",
     "Congress's 'power of the purse' means it controls:",
     ["Federal spending and taxation","Military operations","Judicial appointments","State budgets"],0,
     "Congress controls government spending through its authority over appropriations and revenue."),

    ("Unit 2","Interactions Among Branches","Senate vs. House",
     "Compared to the House, the Senate is considered more deliberative because:",
     ["It has more members","It has unlimited debate and the filibuster","It only considers tax bills","Members serve two-year terms"],1,
     "The Senate's rules allow extended debate, making it a more deliberative body."),

    ("Unit 2","Interactions Among Branches","Logrolling",
     "Logrolling in Congress refers to:",
     ["Filibustering a bill","Members exchanging votes to pass each other's legislation","The president signing a bill into law","Judicial review of legislation"],1,
     "Legislators trade votes on different bills to build coalitions of support."),

    ("Unit 2","Interactions Among Branches","Discharge Petition",
     "A discharge petition is used to:",
     ["Impeach the president","Force a bill out of committee for a floor vote","End a filibuster","Override a veto"],1,
     "If a majority of House members sign a discharge petition, a bill bypasses the committee."),

    ("Unit 2","Interactions Among Branches","Pocket Veto",
     "A pocket veto occurs when:",
     ["The president signs a bill into law","Congress overrides a veto","The president does not sign a bill and Congress adjourns within 10 days","The Supreme Court vetoes a law"],2,
     "If Congress adjourns before 10 days and the president hasn't signed, the bill dies."),

    ("Unit 2","Interactions Among Branches","Judicial Activism",
     "Judicial activism is the philosophy that courts should:",
     ["Only interpret law narrowly","Broadly interpret the Constitution to address social issues","Defer to the legislature always","Avoid ruling on any political questions"],1,
     "Activists believe courts should use their power to advance justice and protect rights."),

    ("Unit 2","Interactions Among Branches","Judicial Restraint",
     "Judicial restraint holds that judges should:",
     ["Broadly interpret rights","Defer to elected branches and avoid overturning laws unless clearly unconstitutional","Always agree with the president","Ignore precedent"],1,
     "Restraint advocates believe courts should not substitute their judgment for that of legislatures."),

    ("Unit 2","Interactions Among Branches","Federalist No. 70",
     "In Federalist No. 70, Alexander Hamilton argued for:",
     ["A plural executive","A weak presidency","An energetic, unitary executive","Eliminating the presidency"],2,
     "Hamilton believed a single, energetic executive was necessary for effective governance."),

    ("Unit 2","Interactions Among Branches","Federalist No. 78",
     "In Federalist No. 78, Hamilton described the judiciary as the:",
     ["Most dangerous branch","Least dangerous branch","Most powerful branch","Only necessary branch"],1,
     "Hamilton argued the judiciary has 'neither force nor will, but merely judgment.'"),

    ("Unit 2","Interactions Among Branches","Executive Privilege",
     "Executive privilege is the claim that the president:",
     ["Is immune from all lawsuits","Can withhold information from Congress and courts for national security","Can fire any government employee","Has the power to declare war"],1,
     "Presidents have claimed the right to keep certain communications confidential."),

    ("Unit 2","Interactions Among Branches","Baker v. Carr",
     "Baker v. Carr (1962) established the principle of:",
     ["Executive privilege","Freedom of the press","'One person, one vote' and justiciability of redistricting","Separation of church and state"],2,
     "The case established that redistricting issues are justiciable and subject to court review."),

    ("Unit 2","Interactions Among Branches","Shaw v. Reno",
     "Shaw v. Reno (1993) ruled that:",
     ["Racial gerrymandering is subject to strict scrutiny","Poll taxes are unconstitutional","The filibuster is unconstitutional","States cannot hold primaries"],0,
     "Bizarrely shaped districts drawn primarily by race violate the Equal Protection Clause."),

    ("Unit 2","Interactions Among Branches","Trustee vs. Delegate",
     "A member of Congress acting as a trustee:",
     ["Votes only according to their constituents' wishes","Uses their own judgment to vote on legislation","Follows the party leader always","Abstains from voting"],1,
     "Trustees exercise independent judgment rather than simply mirroring constituent opinion."),

    ("Unit 2","Interactions Among Branches","Delegate Model",
     "Under the delegate model of representation, a legislator should:",
     ["Vote based on personal beliefs","Vote according to the wishes of their constituents","Follow the president's directives","Ignore public opinion"],1,
     "Delegates act as mouthpieces for the people who elected them."),

    ("Unit 2","Interactions Among Branches","Politico Model",
     "The politico model of representation combines aspects of:",
     ["Only the trustee model","Only the delegate model","Both trustee and delegate models depending on the issue","Neither model"],2,
     "Politicos balance personal judgment and constituent preferences depending on the situation."),

    ("Unit 2","Interactions Among Branches","Divided Government",
     "Divided government occurs when:",
     ["One party controls both Congress and the presidency","Different parties control the presidency and at least one chamber of Congress","The Supreme Court disagrees with Congress","States conflict with federal law"],1,
     "Divided government often leads to gridlock as competing parties struggle to pass legislation."),

    ("Unit 2","Interactions Among Branches","Bureaucratic Rule-Making",
     "Federal agencies create regulations through a process called:",
     ["Adjudication","Rule-making","Filibustering","Gerrymandering"],1,
     "Rule-making allows agencies to establish detailed rules that have the force of law."),

    ("Unit 2","Interactions Among Branches","Independent Regulatory Commissions",
     "Independent regulatory commissions differ from cabinet departments because they:",
     ["Report directly to the president","Operate with more independence from presidential control","Have no authority","Are part of Congress"],1,
     "Independent commissions like the FCC are designed to be insulated from direct presidential influence."),

    ("Unit 2","Interactions Among Branches","Government Corporations",
     "An example of a government corporation is:",
     ["The Department of State","The FBI","The United States Postal Service","The National Guard"],2,
     "Government corporations like USPS provide services that could be offered by the private sector."),

    ("Unit 2","Interactions Among Branches","Congressional Oversight",
     "Congressional oversight of the bureaucracy includes:",
     ["Appointing agency heads","Holding hearings and controlling agency budgets","Issuing executive orders","Filing lawsuits"],1,
     "Congress uses hearings, investigations, and budget control to oversee executive agencies."),

    ("Unit 2","Interactions Among Branches","22nd Amendment",
     "The 22nd Amendment limits the president to:",
     ["One term","Two terms","Three terms","No term limits"],1,
     "Ratified in 1951, the amendment limits presidents to two four-year terms."),

    ("Unit 2","Interactions Among Branches","25th Amendment",
     "The 25th Amendment addresses:",
     ["Congressional term limits","Presidential succession and disability","Voting age","Income tax"],1,
     "The amendment outlines procedures when a president is unable to serve."),

    ("Unit 2","Interactions Among Branches","Gerrymandering",
     "Gerrymandering refers to the practice of:",
     ["Drawing district lines to favor a political party","Lobbying Congress","Filibustering in the Senate","Presidential vetoing"],0,
     "Gerrymandering manipulates district boundaries for political advantage."),

    ("Unit 2","Interactions Among Branches","Pork Barrel Spending",
     "Pork barrel spending refers to:",
     ["Government funding directed to a representative's district to win constituent support","Defense spending only","Foreign aid","Judicial salaries"],0,
     "Members of Congress secure funding for local projects to gain electoral support."),

    ("Unit 2","Interactions Among Branches","Incumbency Advantage",
     "Incumbents in Congress have an advantage because of:",
     ["Term limits","Name recognition, franking privileges, and easier fundraising","Judicial support","Mandatory re-election"],1,
     "Incumbents benefit from visibility, constituent services, and access to donors."),

    ("Unit 2","Interactions Among Branches","Legislation Process (Stimulus)",
     "A bill has been passed by both the House and Senate in different forms. What must happen next?",
     ["The president signs both versions","A conference committee reconciles the two versions","The Supreme Court chooses the better version","The bill dies automatically"],1,
     "A conference committee resolves differences before sending a unified bill for final passage."),

    ("Unit 2","Interactions Among Branches","Cabinet Departments",
     "The president's cabinet serves primarily to:",
     ["Write legislation","Advise the president and lead executive departments","Confirm judicial appointments","Override vetoes"],1,
     "Cabinet members head departments and advise the president on policy."),

    ("Unit 2","Interactions Among Branches","Informal Presidential Powers",
     "Which is considered an informal power of the president?",
     ["Vetoing a bill","Negotiating executive agreements with foreign leaders","Nominating judges","Serving as commander in chief"],1,
     "Executive agreements don't require Senate approval and are an informal expansion of presidential power."),

    # ══════════════════════════════════════════════════════════════
    #  UNIT 3 — Civil Liberties and Civil Rights (100 questions)
    # ══════════════════════════════════════════════════════════════

    ("Unit 3","Civil Liberties and Civil Rights","First Amendment",
     "The First Amendment protects all of the following EXCEPT:",
     ["Freedom of speech","Freedom of religion","Right to bear arms","Freedom of the press"],2,
     "The Second Amendment, not the First, protects the right to bear arms."),

    ("Unit 3","Civil Liberties and Civil Rights","Establishment Clause",
     "The Establishment Clause prohibits the government from:",
     ["Establishing an official religion","Allowing religious practice","Taxing churches","Censoring religious speech"],0,
     "The Establishment Clause creates a separation between government and religion."),

    ("Unit 3","Civil Liberties and Civil Rights","Free Exercise Clause",
     "The Free Exercise Clause protects individuals' right to:",
     ["Practice any religion without government interference","Avoid paying taxes","Ignore criminal laws for religious reasons","Receive government funding for worship"],0,
     "The government generally cannot prohibit religious practice, though neutral laws of general applicability may apply."),

    ("Unit 3","Civil Liberties and Civil Rights","Engel v. Vitale",
     "In Engel v. Vitale (1962), the Supreme Court ruled that:",
     ["Students can pray in school","School-sponsored prayer violates the Establishment Clause","Religious clubs cannot meet in public schools","Teachers must teach creationism"],1,
     "The Court struck down state-composed prayers in public schools."),

    ("Unit 3","Civil Liberties and Civil Rights","Lemon v. Kurtzman",
     "The Lemon test from Lemon v. Kurtzman requires that a law:",
     ["Must promote religion","Have a secular purpose, not advance or inhibit religion, and avoid excessive entanglement","Must benefit all religions equally","Can favor one religion over another"],1,
     "The three-pronged Lemon test guides Establishment Clause cases."),

    ("Unit 3","Civil Liberties and Civil Rights","Tinker v. Des Moines",
     "In Tinker v. Des Moines (1969), the Court ruled that students:",
     ["Have no rights in school","Do not shed their constitutional rights at the schoolhouse gate","Can say anything without consequence","Must follow all school dress codes"],1,
     "The Court protected student symbolic speech (black armbands) that didn't disrupt school."),

    ("Unit 3","Civil Liberties and Civil Rights","Schenck v. United States",
     "Schenck v. United States (1919) established the:",
     ["Right to unlimited speech","Clear and present danger test for limiting speech","Right to protest during wartime","Freedom from censorship"],1,
     "Justice Holmes argued speech creating a 'clear and present danger' can be restricted."),

    ("Unit 3","Civil Liberties and Civil Rights","New York Times v. Sullivan",
     "New York Times v. Sullivan (1964) made it harder for public officials to win libel suits by requiring proof of:",
     ["Any false statement","Actual malice — knowledge that a statement was false or reckless disregard for truth","Intent to harm","Financial damage only"],1,
     "The 'actual malice' standard protects press criticism of public officials."),

    ("Unit 3","Civil Liberties and Civil Rights","Prior Restraint",
     "Prior restraint refers to:",
     ["Punishing speech after it occurs","Government censorship that prevents speech before publication","Regulating commercial speech","Limiting campaign contributions"],1,
     "The Court has generally held that prior restraint is presumptively unconstitutional."),

    ("Unit 3","Civil Liberties and Civil Rights","Second Amendment",
     "The Second Amendment protects:",
     ["Freedom of the press","The right to keep and bear arms","Freedom of religion","The right to a fair trial"],1,
     "The Second Amendment has been interpreted to protect an individual's right to own firearms."),

    ("Unit 3","Civil Liberties and Civil Rights","McDonald v. Chicago",
     "McDonald v. Chicago (2010) incorporated the Second Amendment by ruling that:",
     ["The federal government can ban all guns","States and cities cannot completely ban handgun ownership","Only the military can own weapons","Gun regulations are always unconstitutional"],1,
     "The Court applied the Second Amendment to state and local governments through incorporation."),

    ("Unit 3","Civil Liberties and Civil Rights","Fourth Amendment",
     "The Fourth Amendment protects against:",
     ["Self-incrimination","Cruel punishment","Unreasonable searches and seizures","Double jeopardy"],2,
     "The Fourth Amendment requires probable cause and often warrants for searches."),

    ("Unit 3","Civil Liberties and Civil Rights","Exclusionary Rule",
     "The exclusionary rule means that:",
     ["All evidence is admissible","Evidence obtained illegally cannot be used in court","Defendants cannot testify","Judges can exclude witnesses"],1,
     "Mapp v. Ohio (1961) applied the exclusionary rule to state courts."),

    ("Unit 3","Civil Liberties and Civil Rights","Fifth Amendment",
     "The Fifth Amendment protects individuals from:",
     ["Unreasonable searches","Self-incrimination and double jeopardy","Cruel punishment","Excessive bail"],1,
     "The Fifth Amendment includes the right to remain silent and protection from being tried twice."),

    ("Unit 3","Civil Liberties and Civil Rights","Miranda v. Arizona",
     "Miranda v. Arizona (1966) requires police to:",
     ["Obtain a search warrant before any arrest","Inform suspects of their rights before custodial interrogation","Allow suspects to leave at any time","Provide an attorney at the scene"],1,
     "The Miranda warning ensures suspects know their Fifth and Sixth Amendment rights."),

    ("Unit 3","Civil Liberties and Civil Rights","Sixth Amendment",
     "The Sixth Amendment guarantees the right to:",
     ["Bear arms","Be free from excessive bail","A speedy and public trial with an attorney","Privacy"],2,
     "The Sixth Amendment ensures a speedy trial, an impartial jury, and the right to counsel."),

    ("Unit 3","Civil Liberties and Civil Rights","Gideon v. Wainwright",
     "Gideon v. Wainwright (1963) established that:",
     ["States must provide attorneys for defendants who cannot afford one","The death penalty is cruel and unusual","Police must read Miranda rights","All trials must have a jury"],0,
     "The Court ruled the Sixth Amendment right to counsel applies to state courts."),

    ("Unit 3","Civil Liberties and Civil Rights","Eighth Amendment",
     "The Eighth Amendment prohibits:",
     ["Unreasonable searches","Self-incrimination","Excessive bail, fines, and cruel and unusual punishment","Quartering of soldiers"],2,
     "The Eighth Amendment limits the government's power to punish."),

    ("Unit 3","Civil Liberties and Civil Rights","Right to Privacy",
     "The right to privacy is:",
     ["Explicitly stated in the First Amendment","Not explicitly in the Constitution but inferred from several amendments","Guaranteed by the Tenth Amendment only","Stated in Article III"],1,
     "The Court has found a right to privacy in the penumbras of the 1st, 3rd, 4th, 5th, and 9th Amendments."),

    ("Unit 3","Civil Liberties and Civil Rights","Roe v. Wade",
     "Roe v. Wade (1973) ruled that the right to privacy:",
     ["Does not exist","Is absolute","Includes a woman's decision to have an abortion, subject to state interests","Only applies to medical records"],2,
     "The Court established a trimester framework balancing women's rights and state interests."),

    ("Unit 3","Civil Liberties and Civil Rights","14th Amendment Equal Protection",
     "The Equal Protection Clause of the 14th Amendment requires that:",
     ["States treat all persons within their jurisdiction equally under the law","The federal government cannot tax citizens","Only citizens have rights","States can discriminate based on religion"],0,
     "Equal protection has been the basis for challenging racial, gender, and other discrimination."),

    ("Unit 3","Civil Liberties and Civil Rights","Brown v. Board of Education",
     "Brown v. Board of Education (1954) overturned the 'separate but equal' doctrine by ruling that:",
     ["Schools could remain segregated","Separate educational facilities are inherently unequal","Only private schools could segregate","Integration was optional"],1,
     "The unanimous decision declared racial segregation in public schools unconstitutional."),

    ("Unit 3","Civil Liberties and Civil Rights","Civil Rights Act of 1964",
     "The Civil Rights Act of 1964 prohibited discrimination based on:",
     ["Only race","Only gender","Race, color, religion, sex, and national origin","Age and disability only"],2,
     "The landmark legislation banned discrimination in employment, public accommodations, and federally funded programs."),

    ("Unit 3","Civil Liberties and Civil Rights","Voting Rights Act of 1965",
     "The Voting Rights Act of 1965 was primarily aimed at:",
     ["Lowering the voting age","Eliminating barriers that prevented African Americans from voting","Establishing the Electoral College","Allowing felons to vote"],1,
     "The Act banned literacy tests and authorized federal oversight of elections in discriminatory areas."),

    ("Unit 3","Civil Liberties and Civil Rights","Letter from Birmingham Jail (Stimulus)",
     "\"One who breaks an unjust law must do so openly, lovingly, and with a willingness to accept the penalty.\" — Martin Luther King Jr.\n\nKing is advocating for:",
     ["Violent revolution","Civil disobedience with acceptance of consequences","Ignoring all laws","Working only through the courts"],1,
     "King defended nonviolent civil disobedience as a moral duty."),

    ("Unit 3","Civil Liberties and Civil Rights","Strict Scrutiny",
     "Under strict scrutiny, the government must show that a law:",
     ["Has any rational basis","Is narrowly tailored to serve a compelling government interest","Benefits the majority","Was passed by a supermajority"],1,
     "Strict scrutiny is the highest standard of review, applied to racial classifications and fundamental rights."),

    ("Unit 3","Civil Liberties and Civil Rights","Intermediate Scrutiny",
     "Intermediate scrutiny is typically applied in cases involving:",
     ["Race","National origin","Gender","Fundamental rights"],2,
     "Gender-based classifications are reviewed under intermediate scrutiny."),

    ("Unit 3","Civil Liberties and Civil Rights","Rational Basis Review",
     "Under rational basis review, a law is upheld if it:",
     ["Serves a compelling interest","Is narrowly tailored","Is rationally related to a legitimate government interest","Treats everyone identically"],2,
     "Rational basis is the most deferential standard and applies to most economic and social legislation."),

    ("Unit 3","Civil Liberties and Civil Rights","Affirmative Action",
     "In Grutter v. Bollinger (2003), the Supreme Court ruled that:",
     ["Race can never be considered in admissions","Race can be one factor in a holistic admissions process to achieve diversity","Quotas are acceptable","Affirmative action is always unconstitutional"],1,
     "The Court upheld the use of race as one factor in university admissions."),

    ("Unit 3","Civil Liberties and Civil Rights","Title IX",
     "Title IX of the Education Amendments of 1972 prohibits:",
     ["Racial discrimination in voting","Gender discrimination in federally funded education programs","Age discrimination in employment","Disability discrimination in housing"],1,
     "Title IX ensures equal access to educational opportunities regardless of gender."),

    ("Unit 3","Civil Liberties and Civil Rights","Due Process",
     "Procedural due process requires that the government:",
     ["Never enforce any law","Follow fair procedures before depriving someone of life, liberty, or property","Allow everyone to vote in all elections","Provide free education to all"],1,
     "The 5th and 14th Amendments require fair legal proceedings."),

    ("Unit 3","Civil Liberties and Civil Rights","Substantive Due Process",
     "Substantive due process protects individuals from:",
     ["Only procedural errors","Government actions that are arbitrary regardless of procedures followed","Criminal prosecution","All forms of taxation"],1,
     "Substantive due process limits what the government can do, not just how it does it."),

    ("Unit 3","Civil Liberties and Civil Rights","Wisconsin v. Yoder",
     "In Wisconsin v. Yoder (1972), the Court ruled that:",
     ["All children must attend public school","Amish families could withdraw children from school after 8th grade on religious grounds","Religious exemptions never apply to education","Home schooling is unconstitutional"],1,
     "The Free Exercise Clause protected the Amish practice of ending formal education early."),

    ("Unit 3","Civil Liberties and Civil Rights","Symbolic Speech",
     "Which Supreme Court case protected symbolic speech in the form of flag burning?",
     ["Schenck v. United States","Texas v. Johnson","Tinker v. Des Moines","Brandenburg v. Ohio"],1,
     "Texas v. Johnson (1989) ruled flag burning is protected expression under the First Amendment."),

    ("Unit 3","Civil Liberties and Civil Rights","Hate Speech",
     "Under current First Amendment jurisprudence, hate speech is:",
     ["Never protected","Generally protected unless it incites imminent lawless action","Always a criminal offense","Regulated by the FCC"],1,
     "The Brandenburg test protects even offensive speech unless it directly incites imminent violence."),

    ("Unit 3","Civil Liberties and Civil Rights","15th Amendment",
     "The 15th Amendment prohibits denying the right to vote based on:",
     ["Gender","Age","Race, color, or previous condition of servitude","Property ownership"],2,
     "Ratified in 1870, the 15th Amendment extended voting rights to African American men."),

    ("Unit 3","Civil Liberties and Civil Rights","19th Amendment",
     "The 19th Amendment granted:",
     ["Freedom of speech to all","Voting rights to women","Abolition of slavery","Equal protection under law"],1,
     "Ratified in 1920, the 19th Amendment prohibited denying the vote based on sex."),

    ("Unit 3","Civil Liberties and Civil Rights","24th Amendment",
     "The 24th Amendment eliminated:",
     ["The Electoral College","Poll taxes in federal elections","Literacy tests","The filibuster"],1,
     "Poll taxes had been used to disenfranchise poor and minority voters."),

    ("Unit 3","Civil Liberties and Civil Rights","Selective Incorporation Detail",
     "Which case incorporated the right to counsel to the states?",
     ["Gideon v. Wainwright","Mapp v. Ohio","Miranda v. Arizona","Roe v. Wade"],0,
     "Gideon v. Wainwright (1963) applied the Sixth Amendment right to counsel to state courts."),

    ("Unit 3","Civil Liberties and Civil Rights","Mapp v. Ohio",
     "Mapp v. Ohio (1961) applied the exclusionary rule to the states, meaning:",
     ["All evidence is always admissible in state courts","Illegally obtained evidence cannot be used in state criminal trials","States can create their own search rules","Only federal courts follow the Fourth Amendment"],1,
     "The ruling extended the Fourth Amendment protection against illegal searches to state proceedings."),

    ("Unit 3","Civil Liberties and Civil Rights","Citizens United v. FEC",
     "Citizens United v. FEC (2010) ruled that:",
     ["Corporations cannot participate in politics","Political spending by corporations is protected under the First Amendment","Campaign contributions have no limits","Only individuals can donate to campaigns"],1,
     "The Court held that restricting independent political expenditures by corporations violates free speech."),

    ("Unit 3","Civil Liberties and Civil Rights","Cruel and Unusual Punishment",
     "Which case addressed whether the death penalty constitutes cruel and unusual punishment?",
     ["Gideon v. Wainwright","Miranda v. Arizona","Furman v. Georgia","Mapp v. Ohio"],2,
     "Furman v. Georgia (1972) imposed a moratorium on the death penalty as then applied."),

    ("Unit 3","Civil Liberties and Civil Rights","13th Amendment",
     "The 13th Amendment:",
     ["Abolished slavery and involuntary servitude","Granted citizenship to all born in the U.S.","Guaranteed equal protection","Extended voting rights to African Americans"],0,
     "Ratified in 1865, the 13th Amendment ended slavery in the United States."),

    ("Unit 3","Civil Liberties and Civil Rights","De Facto vs. De Jure Segregation",
     "De facto segregation differs from de jure segregation because it:",
     ["Is required by law","Exists in practice without legal mandate","Only occurs in the South","Was ended by Brown v. Board"],1,
     "De facto segregation arises from social and economic conditions rather than legislation."),

    ("Unit 3","Civil Liberties and Civil Rights","Plessy v. Ferguson",
     "Plessy v. Ferguson (1896) established the doctrine of:",
     ["Judicial review","Separate but equal","Selective incorporation","Strict scrutiny"],1,
     "The 'separate but equal' doctrine allowed legally mandated racial segregation until Brown overturned it."),

    # ══════════════════════════════════════════════════════════════
    #  UNIT 4 — American Political Ideologies and Beliefs (100 qs)
    # ══════════════════════════════════════════════════════════════

    ("Unit 4","American Political Ideologies and Beliefs","Liberal vs. Conservative",
     "On economic issues, liberals generally favor:",
     ["Government regulation and social welfare programs","Lower taxes and less regulation","Eliminating all government programs","Privatizing Social Security"],0,
     "Liberals typically support government intervention to reduce inequality."),

    ("Unit 4","American Political Ideologies and Beliefs","Conservative Economic Views",
     "Conservatives typically support:",
     ["Higher taxes on the wealthy","Expanding government programs","Free-market principles and limited government regulation","Nationalizing industries"],2,
     "Conservatives generally favor a smaller role for government in the economy."),

    ("Unit 4","American Political Ideologies and Beliefs","Libertarian Ideology",
     "Libertarians generally believe in:",
     ["Strong government regulation","Extensive social welfare","Minimal government intervention in both economic and social affairs","Government control of the economy"],2,
     "Libertarians advocate for individual freedom and limited government in all areas."),

    ("Unit 4","American Political Ideologies and Beliefs","Political Socialization",
     "The most important agent of political socialization is typically:",
     ["The family","The media","Schools","Peer groups"],0,
     "Family is usually the strongest early influence on political attitudes and party identification."),

    ("Unit 4","American Political Ideologies and Beliefs","Media Influence",
     "The media's role in political socialization includes:",
     ["Having no influence on public opinion","Shaping the public agenda through coverage choices","Directly controlling how people vote","Replacing family as the primary influence"],1,
     "Media helps set the political agenda by deciding what issues receive coverage."),

    ("Unit 4","American Political Ideologies and Beliefs","Public Opinion Polls",
     "A scientific public opinion poll requires:",
     ["Asking only people who volunteer","A random sample representative of the population","Surveying only political experts","Asking leading questions"],1,
     "Random sampling ensures the poll accurately represents the broader population."),

    ("Unit 4","American Political Ideologies and Beliefs","Sampling Error",
     "The margin of error in a poll reflects:",
     ["How biased the questions are","The range within which the true value likely falls","How many people refused to answer","The cost of conducting the poll"],1,
     "Margin of error indicates the statistical uncertainty in poll results."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology Spectrum",
     "On the political spectrum, someone who favors tradition, lower taxes, and a strong military is likely:",
     ["Liberal","Libertarian","Conservative","Socialist"],2,
     "These positions align with mainstream conservative ideology."),

    ("Unit 4","American Political Ideologies and Beliefs","Gender Gap",
     "The 'gender gap' in American politics refers to:",
     ["Men and women voting at different rates","Differences in political opinions and voting patterns between men and women","Women being unable to run for office","Equal representation in Congress"],1,
     "Women tend to lean more Democratic, while men tend to lean more Republican."),

    ("Unit 4","American Political Ideologies and Beliefs","Generational Effects",
     "Political events experienced during young adulthood can shape a generation's political views. This is called:",
     ["Political apathy","Generational effect","Random socialization","Ideological purity"],1,
     "Major events like wars, recessions, or movements can define a generation's politics."),

    ("Unit 4","American Political Ideologies and Beliefs","Entitlement Programs",
     "Social Security and Medicare are called entitlement programs because:",
     ["Only certain people qualify based on need","Eligible individuals are legally entitled to benefits","They require annual congressional approval","They are funded by state governments"],1,
     "Entitlements guarantee benefits to all who meet eligibility criteria."),

    ("Unit 4","American Political Ideologies and Beliefs","Federal Budget",
     "The largest portion of mandatory federal spending goes to:",
     ["Defense","Social Security and Medicare","Education","Foreign aid"],1,
     "Entitlement programs like Social Security and Medicare dominate mandatory spending."),

    ("Unit 4","American Political Ideologies and Beliefs","Deficit vs. Debt",
     "The national debt differs from the annual deficit because the debt:",
     ["Is the total accumulation of all past deficits","Is always decreasing","Only includes foreign borrowing","Is the same as the deficit"],0,
     "The national debt is the cumulative total of all annual budget deficits over time."),

    ("Unit 4","American Political Ideologies and Beliefs","Supply-Side Economics",
     "Supply-side economics argues that economic growth is best achieved by:",
     ["Raising taxes on corporations","Increasing government spending on social programs","Lowering taxes to stimulate investment and production","Imposing trade tariffs"],2,
     "Supply-siders believe tax cuts incentivize investment and economic growth."),

    ("Unit 4","American Political Ideologies and Beliefs","Keynesian Economics",
     "Keynesian economics advocates that during a recession, the government should:",
     ["Cut spending dramatically","Increase spending to stimulate demand","Do nothing","Raise interest rates"],1,
     "Keynes argued government spending can compensate for reduced private demand."),

    ("Unit 4","American Political Ideologies and Beliefs","Social Policy Views",
     "On social issues like same-sex marriage, conservatives tend to:",
     ["Support expanded rights","Oppose changes to traditional definitions","Have no opinion","Favor government mandates"],1,
     "Social conservatives typically support traditional values and institutions."),

    ("Unit 4","American Political Ideologies and Beliefs","Education Policy",
     "Conservatives generally favor education policies that include:",
     ["Increased federal control","School choice through vouchers and charter schools","Eliminating private schools","Mandatory national curriculum"],1,
     "Conservatives often support market-based approaches to education."),

    ("Unit 4","American Political Ideologies and Beliefs","Environmental Policy",
     "Liberals generally support environmental regulations because they believe:",
     ["The free market will solve environmental problems","Government action is necessary to protect public health and the environment","Environmental issues are not important","Only state governments should regulate"],1,
     "Liberals typically favor federal environmental regulations and climate action."),

    ("Unit 4","American Political Ideologies and Beliefs","Immigration Views",
     "A political candidate who supports a path to citizenship for undocumented immigrants likely holds:",
     ["Conservative views on immigration","Libertarian economic views","Liberal views on immigration","Populist views"],2,
     "Support for a path to citizenship is associated with liberal immigration policy."),

    ("Unit 4","American Political Ideologies and Beliefs","Healthcare Policy",
     "Which statement best reflects a liberal view on healthcare?",
     ["The government should provide universal healthcare coverage","Healthcare should be entirely privatized","The government should not be involved in healthcare","Only the wealthy should have access to healthcare"],0,
     "Liberals generally support expanding government's role in providing healthcare."),

    ("Unit 4","American Political Ideologies and Beliefs","Gun Control",
     "Liberals are more likely than conservatives to support:",
     ["Expanded gun rights","Stricter gun control legislation","Eliminating all gun laws","Arming teachers"],1,
     "Liberals tend to favor gun safety regulations and restrictions."),

    ("Unit 4","American Political Ideologies and Beliefs","Criminal Justice Reform",
     "Liberals are more likely to advocate for:",
     ["Mandatory minimum sentences","Expanding the death penalty","Reforming the criminal justice system to reduce mass incarceration","Increasing police funding without oversight"],2,
     "Liberals often emphasize rehabilitation and addressing systemic inequities in criminal justice."),

    ("Unit 4","American Political Ideologies and Beliefs","Fiscal Policy",
     "Fiscal policy involves the government using:",
     ["Interest rates to control inflation","Taxation and spending to influence the economy","Military force","Judicial appointments"],1,
     "Fiscal policy uses government revenue and expenditure as tools to manage economic conditions."),

    ("Unit 4","American Political Ideologies and Beliefs","Monetary Policy",
     "Monetary policy is primarily managed by:",
     ["Congress","The president","The Federal Reserve","State governments"],2,
     "The Federal Reserve controls the money supply and interest rates."),

    ("Unit 4","American Political Ideologies and Beliefs","Trade Policy",
     "Free trade agreements are generally supported by those who believe:",
     ["All trade should be banned","Tariffs protect domestic jobs","Open markets benefit consumers through lower prices and more choices","Only exports matter"],2,
     "Free trade advocates argue that reducing barriers benefits economies overall."),

    ("Unit 4","American Political Ideologies and Beliefs","Welfare Policy",
     "TANF (Temporary Assistance for Needy Families) differs from earlier welfare because it:",
     ["Has no time limits","Includes work requirements and time limits","Is available to everyone","Provides unlimited benefits"],1,
     "The 1996 welfare reform imposed work requirements and five-year limits."),

    ("Unit 4","American Political Ideologies and Beliefs","Populism",
     "Populism as a political ideology emphasizes:",
     ["Elite rule","The concerns and power of ordinary people against the elite","Judicial supremacy","Corporate interests"],1,
     "Populists position themselves as champions of the common people against powerful elites."),

    ("Unit 4","American Political Ideologies and Beliefs","Neoconservatism",
     "Neoconservatives are most associated with support for:",
     ["Isolationist foreign policy","Promoting democracy abroad through an active foreign policy including military force","Reducing defense spending","Pacifism"],1,
     "Neoconservatives advocate for an assertive U.S. role in international affairs."),

    ("Unit 4","American Political Ideologies and Beliefs","Push Polls",
     "Push polls are problematic because they:",
     ["Use random sampling","Ask neutral questions","Use leading questions designed to influence respondents' opinions rather than measure them","Have large sample sizes"],2,
     "Push polls are a form of propaganda disguised as polling."),

    ("Unit 4","American Political Ideologies and Beliefs","Benchmark Polls",
     "A benchmark poll is typically conducted:",
     ["After an election","At the start of a campaign to establish baseline support","Only by the media","During voting"],1,
     "Campaigns use benchmark polls to understand their starting position with voters."),

    ("Unit 4","American Political Ideologies and Beliefs","Exit Polls",
     "Exit polls are conducted:",
     ["Before an election","As voters leave polling places on Election Day","Only by mail","A month after elections"],1,
     "Media organizations survey voters leaving polls to project outcomes and analyze voting patterns."),

    ("Unit 4","American Political Ideologies and Beliefs","Tracking Polls",
     "Tracking polls differ from other polls because they:",
     ["Are conducted only once","Survey the same group over time to detect trends","Use very small samples","Are always accurate"],1,
     "Tracking polls continuously monitor public opinion to identify changes over time."),

    ("Unit 4","American Political Ideologies and Beliefs","Political Ideology Formation (Stimulus)",
     "A survey shows that 65% of Americans aged 18-29 support government-funded healthcare, while only 35% of those over 65 do. This difference is best explained by:",
     ["Sampling error","Generational differences in political socialization","Random chance","Media bias"],1,
     "Different generations often develop different political attitudes based on their experiences."),

    ("Unit 4","American Political Ideologies and Beliefs","Party Identification",
     "The strongest predictor of how someone will vote is:",
     ["Their income level","Their education level","Their party identification","Their age"],2,
     "Party identification is the single best predictor of vote choice."),

    ("Unit 4","American Political Ideologies and Beliefs","Realignment",
     "A political realignment occurs when:",
     ["Voters shift party loyalties in a lasting way, often due to major issues","An election is contested","A third party wins","Voter turnout decreases"],0,
     "Realignments mark fundamental, lasting shifts in the party system."),

    ("Unit 4","American Political Ideologies and Beliefs","Social Conservatism",
     "A social conservative would most likely support:",
     ["Legalization of all drugs","Traditional family values and opposition to abortion","Expanding LGBTQ+ protections","Eliminating religious institutions"],1,
     "Social conservatives emphasize traditional moral and family values."),

    ("Unit 4","American Political Ideologies and Beliefs","Progressivism",
     "Progressives generally advocate for:",
     ["Maintaining the status quo","Government-led social and economic reform to address inequality","Eliminating all regulations","Reducing the size of government"],1,
     "Progressives push for systemic reforms to create a more equitable society."),

    ("Unit 4","American Political Ideologies and Beliefs","Tax Policy Views",
     "A progressive tax system means:",
     ["Everyone pays the same rate","Higher-income earners pay a higher percentage","Lower-income earners pay more","Taxes are voluntary"],1,
     "Progressive taxation increases rates as income rises."),

    ("Unit 4","American Political Ideologies and Beliefs","Flat Tax",
     "Supporters of a flat tax argue that it:",
     ["Is more complex than the current system","Is simpler and treats all taxpayers equally","Only benefits the wealthy","Should replace all government revenue"],1,
     "Flat tax advocates emphasize simplicity and equal treatment."),

    ("Unit 4","American Political Ideologies and Beliefs","Policy Mood (Stimulus)",
     "A graph shows public support for government spending increasing during a recession and decreasing during economic booms. This pattern demonstrates:",
     ["The public's policy mood shifts in response to economic conditions","People always want more spending","Polls are unreliable","The media controls public opinion"],0,
     "Public opinion on government's role often shifts with economic circumstances."),

    # ══════════════════════════════════════════════════════════════
    #  UNIT 5 — Political Participation (100 questions)
    # ══════════════════════════════════════════════════════════════

    ("Unit 5","Political Participation","Voter Turnout",
     "Which factor most increases voter turnout?",
     ["Being young","Higher education levels","Living in a rural area","Registering on Election Day"],1,
     "Education is one of the strongest predictors of voter participation."),

    ("Unit 5","Political Participation","Primary Elections",
     "In a closed primary election:",
     ["Any voter can participate regardless of party","Only registered party members can vote in that party's primary","The general public votes for all candidates","There are no candidates"],1,
     "Closed primaries restrict participation to voters registered with the party."),

    ("Unit 5","Political Participation","Open Primaries",
     "An open primary allows:",
     ["Only party members to vote","Voters to participate in any party's primary regardless of registration","Only independents to vote","Candidates from all parties on one ballot"],1,
     "Open primaries do not require voters to be registered with a particular party."),

    ("Unit 5","Political Participation","Electoral College",
     "The Electoral College system means that presidential elections are decided by:",
     ["Direct popular vote","Electoral votes allocated to states based on congressional representation","A vote in Congress","The Supreme Court"],1,
     "Each state gets electors equal to its total number of House and Senate members."),

    ("Unit 5","Political Participation","Winner-Take-All",
     "Most states use a winner-take-all system for the Electoral College, meaning:",
     ["Electoral votes are split proportionally","All of a state's electoral votes go to the candidate who wins the popular vote in that state","Only the winning party's voters count","Third parties always get some votes"],1,
     "In 48 states, the popular vote winner receives all electoral votes."),

    ("Unit 5","Political Participation","Two-Party System",
     "The United States has a two-party system primarily because of:",
     ["The Constitution mandating two parties","Winner-take-all elections and single-member districts","Federal law banning third parties","Voters preferring only two choices"],1,
     "Single-member districts with plurality voting (Duverger's Law) favor two major parties."),

    ("Unit 5","Political Participation","Third Parties",
     "Third parties in the U.S. are significant because they:",
     ["Often win presidential elections","Bring new issues to the political agenda and can influence major party platforms","Are constitutionally protected","Have equal media coverage"],1,
     "Third parties serve as idea incubators even though they rarely win major offices."),

    ("Unit 5","Political Participation","Interest Groups",
     "Interest groups differ from political parties because they:",
     ["Run candidates for office","Seek to influence policy without running candidates","Have no political goals","Are funded by the government"],1,
     "Interest groups lobby and advocate for policy positions rather than nominating candidates."),

    ("Unit 5","Political Participation","PACs",
     "Political Action Committees (PACs) are organizations that:",
     ["Run for political office","Raise money to donate directly to candidates' campaigns","Are illegal","Can donate unlimited amounts to candidates"],1,
     "PACs pool contributions to support or oppose candidates within legal contribution limits."),

    ("Unit 5","Political Participation","Super PACs",
     "Super PACs differ from traditional PACs because they:",
     ["Cannot accept any donations","Can raise and spend unlimited money on independent expenditures but cannot coordinate with campaigns","Can donate directly to candidates","Are run by the government"],1,
     "Super PACs emerged after Citizens United and SpeechNow.org v. FEC."),

    ("Unit 5","Political Participation","Lobbying",
     "Lobbying is the practice of:",
     ["Running for office","Attempting to influence government officials on behalf of an interest group or cause","Voting in elections","Filing lawsuits"],1,
     "Lobbyists represent various interests and try to shape legislation and policy."),

    ("Unit 5","Political Participation","Motor Voter Act",
     "The National Voter Registration Act (Motor Voter, 1993) was designed to:",
     ["Make it easier to register to vote at government offices like the DMV","Eliminate voter registration","Allow online voting","Require voter ID"],0,
     "The Act simplified registration by requiring states to offer it at motor vehicle and other agencies."),

    ("Unit 5","Political Participation","Voter ID Laws",
     "Critics of strict voter ID laws argue that they:",
     ["Increase turnout","Disproportionately burden low-income and minority voters","Have no effect","Are required by the Constitution"],1,
     "Opponents say strict ID requirements create barriers for those less likely to have photo identification."),

    ("Unit 5","Political Participation","Gerrymandering Effects",
     "Partisan gerrymandering can reduce electoral competition by:",
     ["Creating more competitive districts","Drawing districts where one party has a safe majority","Eliminating the Electoral College","Increasing voter turnout"],1,
     "Gerrymandered districts often guarantee outcomes, reducing competition."),

    ("Unit 5","Political Participation","Campaign Finance",
     "The Federal Election Campaign Act (FECA) requires:",
     ["Unlimited donations to candidates","Disclosure of campaign contributions and spending","No limits on anything","Government-funded campaigns only"],1,
     "FECA established reporting requirements and contribution limits."),

    ("Unit 5","Political Participation","Buckley v. Valeo",
     "Buckley v. Valeo (1976) ruled that:",
     ["All campaign spending can be limited","Spending money on campaigns is a form of protected speech","Corporations cannot participate in politics","Public financing is unconstitutional"],1,
     "The Court ruled that limiting campaign expenditures violates the First Amendment."),

    ("Unit 5","Political Participation","Media in Campaigns",
     "The media's role in campaigns includes all of the following EXCEPT:",
     ["Setting the agenda","Providing free airtime to all candidates equally","Fact-checking claims","Hosting debates"],1,
     "Media do not provide free, equal airtime; paid advertising and earned media coverage are unequal."),

    ("Unit 5","Political Participation","Horse Race Coverage",
     "Horse race journalism in political campaigns focuses on:",
     ["Policy details","Who is ahead in polls rather than policy substance","Historical context","Legislative analysis"],1,
     "Horse race coverage emphasizes polling numbers and campaign strategy over issues."),

    ("Unit 5","Political Participation","Swing States",
     "Swing states are important in presidential elections because they:",
     ["Always vote for the same party","Could be won by either major party candidate","Have the most electoral votes","Are the smallest states"],1,
     "Candidates focus resources on competitive states that could tip the electoral college."),

    ("Unit 5","Political Participation","Midterm Elections",
     "Midterm elections typically result in:",
     ["Higher turnout than presidential elections","The president's party gaining seats","No change in party control","The president's party losing seats in Congress"],3,
     "The president's party historically loses congressional seats during midterms."),

    ("Unit 5","Political Participation","Ballot Initiatives",
     "A ballot initiative allows:",
     ["The president to propose legislation","Citizens to vote directly on proposed laws or amendments","Congress to override state laws","Judges to create new laws"],1,
     "Ballot initiatives are a form of direct democracy available in many states."),

    ("Unit 5","Political Participation","Recall Elections",
     "A recall election allows voters to:",
     ["Elect additional representatives","Remove an elected official before their term ends","Override a Supreme Court decision","Amend the Constitution"],1,
     "Recalls are a mechanism for voters to hold officials accountable between regular elections."),

    ("Unit 5","Political Participation","Party Platforms",
     "A political party's platform is:",
     ["Its list of candidates","A statement of the party's positions on issues and policy goals","Its fundraising strategy","Its organizational chart"],1,
     "The platform outlines the party's official stances on major issues."),

    ("Unit 5","Political Participation","National Conventions",
     "National party conventions serve to:",
     ["Pass legislation","Formally nominate presidential candidates and adopt party platforms","Elect members of Congress","Confirm judicial appointments"],1,
     "Conventions are the culmination of the nomination process for presidential candidates."),

    ("Unit 5","Political Participation","Caucuses",
     "Iowa's caucus system differs from a primary because it involves:",
     ["Secret ballot voting at polling places","Voters gathering in groups to publicly discuss and select candidates","Only elected officials voting","No voter participation"],1,
     "Caucuses are participatory meetings rather than simple secret-ballot elections."),

    ("Unit 5","Political Participation","Delegate Selection",
     "In the Democratic Party, superdelegates are:",
     ["Elected through primaries","Party leaders and elected officials who can support any candidate at the convention","Required to follow state primary results","Chosen by the Republican Party"],1,
     "Superdelegates are unpledged delegates with independent voting discretion at the convention."),

    ("Unit 5","Political Participation","Social Media in Politics",
     "Social media has changed political campaigns by:",
     ["Eliminating the need for fundraising","Allowing candidates to communicate directly with voters and mobilize support","Replacing traditional media entirely","Making campaigns more expensive"],1,
     "Social media enables direct engagement, rapid fundraising, and grassroots mobilization."),

    ("Unit 5","Political Participation","Negative Campaigning",
     "Research on negative campaigning suggests that it:",
     ["Has no effect on voters","Can be effective in lowering opponents' favorability but may also depress turnout","Always increases voter turnout","Is illegal"],1,
     "Negative ads can shape perceptions but may also contribute to voter cynicism."),

    ("Unit 5","Political Participation","Issue Networks",
     "Issue networks differ from iron triangles because they:",
     ["Are more rigid and exclusive","Include a broader, more fluid range of participants involved in a policy area","Only involve government officials","Never change membership"],1,
     "Issue networks are more open and dynamic than the closed iron triangle relationship."),

    ("Unit 5","Political Participation","Rational Choice Voting",
     "The rational choice model suggests voters will:",
     ["Always vote for the incumbent","Vote for the candidate whose policies best serve their self-interest","Vote randomly","Never participate in elections"],1,
     "Rational choice theory assumes voters make calculated decisions to maximize their benefit."),

    ("Unit 5","Political Participation","Retrospective Voting",
     "Retrospective voting means voters:",
     ["Look at candidates' future promises","Evaluate candidates based on past performance","Only vote in retrospect","Never consider incumbents"],1,
     "Retrospective voters judge whether things have gotten better or worse under current leadership."),

    ("Unit 5","Political Participation","Prospective Voting",
     "Prospective voting involves:",
     ["Voting based on what a candidate promises to do in the future","Voting based on past performance","Random selection","Straight-ticket voting only"],0,
     "Prospective voters choose based on candidates' proposed policies."),

    ("Unit 5","Political Participation","Straight-Ticket Voting",
     "Straight-ticket voting refers to:",
     ["Splitting votes between parties","Voting for candidates of the same party for all offices on the ballot","Voting only for president","Not voting at all"],1,
     "Some voters choose all candidates from one party."),

    ("Unit 5","Political Participation","Split-Ticket Voting",
     "Split-ticket voting occurs when a voter:",
     ["Votes for candidates of different parties for various offices","Only votes in primaries","Writes in candidates","Votes for the same party throughout"],0,
     "Split-ticket voters may choose a Republican president and a Democratic senator, for example."),

    ("Unit 5","Political Participation","Party Dealignment",
     "Party dealignment refers to:",
     ["Voters becoming more strongly partisan","A decline in party loyalty and an increase in independent voters","The merger of two parties","A constitutional amendment about parties"],1,
     "Dealignment occurs when voters move away from strong party identification."),

    ("Unit 5","Political Participation","Linkage Institutions",
     "Linkage institutions connect citizens to government. Examples include:",
     ["Only the Supreme Court","Political parties, interest groups, media, and elections","Only the military","Only bureaucratic agencies"],1,
     "Linkage institutions are the channels through which public preferences are communicated to government."),

    ("Unit 5","Political Participation","Get-Out-the-Vote (GOTV)",
     "Get-out-the-vote efforts are most effective when they:",
     ["Use television ads alone","Involve personal contact such as door-to-door canvassing","Ignore social media","Target only wealthy voters"],1,
     "Research shows personal, face-to-face contact is the most effective GOTV method."),

    ("Unit 5","Political Participation","Civic Participation",
     "Beyond voting, citizens participate in democracy through:",
     ["Only paying taxes","Contacting officials, protesting, volunteering, and joining interest groups","Watching the news only","Doing nothing"],1,
     "Political participation encompasses many activities beyond the ballot box."),

    ("Unit 5","Political Participation","Voter Turnout Factors (Stimulus)",
     "Data shows that voter turnout in the 2020 presidential election was approximately 66%, the highest since 1900. Which factor best explains the increase?",
     ["Fewer candidates running","Expanded access to early and mail-in voting during the pandemic","Mandatory voting laws","Elimination of the Electoral College"],1,
     "The pandemic prompted expanded mail-in and early voting options, increasing accessibility."),

    ("Unit 5","Political Participation","Campaign Strategy (Stimulus)",
     "A campaign manager sees polling data showing their candidate trails by 15 points among suburban women. The BEST strategic response would be to:",
     ["Ignore that demographic entirely","Focus resources on a demographic where the candidate already leads","Develop targeted messaging and outreach to suburban women on issues they prioritize","Withdraw from the race"],2,
     "Effective campaigns use data to target persuadable demographics with relevant messaging."),

    ("Unit 5","Political Participation","26th Amendment",
     "The 26th Amendment lowered the voting age to:",
     ["21","16","25","18"],3,
     "Ratified in 1971, it gave 18-year-olds the right to vote, partly in response to the Vietnam War draft."),

    ("Unit 5","Political Participation","Franking Privilege",
     "The franking privilege allows members of Congress to:",
     ["Vote in other districts","Send mail to constituents at no personal cost, using government funds","Accept unlimited campaign donations","Skip committee meetings"],1,
     "Franking helps incumbents maintain contact with constituents using taxpayer-funded mailings."),

    ("Unit 5","Political Participation","Soft Money",
     "Before the Bipartisan Campaign Reform Act (BCRA), 'soft money' referred to:",
     ["Money donated directly to candidates","Unregulated donations to political parties for party-building activities","Government-funded campaign grants","Small individual contributions"],1,
     "BCRA (McCain-Feingold) banned unlimited soft money contributions to national parties."),

    ("Unit 5","Political Participation","Dark Money",
     "Dark money in politics refers to:",
     ["Government-funded campaigns","Political spending by nonprofit organizations that do not disclose donors","PAC contributions","Small-dollar donations"],1,
     "Dark money groups can influence elections without revealing their funding sources."),

    ("Unit 5","Political Participation","Voter Suppression",
     "Historically, voter suppression tactics included:",
     ["Expanding early voting","Poll taxes, literacy tests, and grandfather clauses","Automatic voter registration","Same-day registration"],1,
     "These tactics were used primarily to prevent African Americans from voting in the Jim Crow era."),

    ("Unit 5","Political Participation","Battleground Strategy (Stimulus)",
     "A map shows a presidential candidate spending 80% of campaign funds in 6 states. This strategy reflects:",
     ["A national campaign approach","The importance of swing states in the Electoral College system","A focus on safe states","Ignoring the Electoral College"],1,
     "Candidates concentrate resources in competitive states that could determine the electoral outcome."),

    ("Unit 5","Political Participation","Front-Loading",
     "Front-loading in the primary process refers to:",
     ["States moving their primaries to earlier dates to gain more influence","Candidates spending all money at the end","Media ignoring early states","Superdelegates voting first"],0,
     "States schedule early primaries to attract candidate attention and media coverage."),

    ("Unit 5","Political Participation","527 Organizations",
     "527 organizations are:",
     ["Government agencies","Tax-exempt groups that engage in political activities like voter mobilization","Part of the judicial branch","Local school boards"],1,
     "Named after the tax code section, 527s can raise unlimited funds for political activities."),

    # ══════════════════════════════════════════════════════════════
    #  ADDITIONAL QUESTIONS TO REACH 500 — Mixed across all units
    # ══════════════════════════════════════════════════════════════

    # Unit 1 additions
    ("Unit 1","Foundations of American Democracy","Federalism Debate (Stimulus)",
     "\"The powers delegated by the proposed Constitution to the federal government are few and defined. Those which are to remain in the State governments are numerous and indefinite.\" — James Madison, Federalist No. 45\n\nMadison is arguing that:",
     ["The federal government will dominate the states","State governments will retain significant authority under the new Constitution","The Constitution eliminates state power","Federal power is unlimited"],1,
     "Madison sought to reassure skeptics that states would keep broad powers."),

    ("Unit 1","Foundations of American Democracy","Supremacy in Practice",
     "When a state law conflicts with a valid federal law, what happens?",
     ["The state law takes precedence","Both laws are enforced equally","The federal law prevails under the Supremacy Clause","The Supreme Court automatically intervenes"],2,
     "Article VI establishes that federal law overrides conflicting state legislation."),

    ("Unit 1","Foundations of American Democracy","Constitutional Interpretation",
     "The 'living Constitution' approach holds that the Constitution should be:",
     ["Interpreted exactly as written","Interpreted in light of contemporary values and circumstances","Never amended","Read only by judges"],1,
     "Living constitutionalists believe the document must evolve with changing times."),

    ("Unit 1","Foundations of American Democracy","Originalism",
     "Originalists believe the Constitution should be interpreted based on:",
     ["The original meaning understood at the time of ratification","Modern societal needs","International law","Congressional intent alone"],0,
     "Originalists seek to apply the Framers' intended meaning."),

    ("Unit 1","Foundations of American Democracy","Confederal vs. Federal",
     "A confederal system differs from a federal system because in a confederal system:",
     ["The central government is all-powerful","Power resides primarily with the individual states, with a weak central authority","There is no government","States do not exist"],1,
     "Confederal systems give most power to subnational units, unlike federal systems."),

    ("Unit 1","Foundations of American Democracy","Mandates and Conditions",
     "Federal mandates differ from conditions of aid because mandates:",
     ["Require state action regardless of federal funding","Are voluntary","Only apply to the judiciary","Do not affect state governments"],0,
     "Mandates compel compliance whether or not states receive federal funds."),

    ("Unit 1","Foundations of American Democracy","Interstate Commerce",
     "The Gibbons v. Ogden (1824) decision strengthened federal power by ruling that:",
     ["States control all commerce","Congress has broad authority to regulate interstate commerce including navigation","Only the president can regulate trade","Commerce stops at state borders"],1,
     "The ruling broadly defined 'commerce' and affirmed federal power over interstate trade."),

    ("Unit 1","Foundations of American Democracy","New Federalism",
     "New Federalism, championed by Presidents Nixon and Reagan, emphasized:",
     ["Expanding federal programs","Shifting power and responsibility back to state governments","Eliminating the states","Creating new federal agencies"],1,
     "New Federalism sought to reduce federal control and return authority to the states."),

    # Unit 2 additions
    ("Unit 2","Interactions Among Branches","Congressional Leadership",
     "The Senate Majority Leader is influential because they:",
     ["Are constitutionally the head of the Senate","Control the Senate's legislative schedule and floor agenda","Can override presidential vetoes","Appoint Supreme Court justices"],1,
     "The Majority Leader shapes what legislation reaches the Senate floor."),

    ("Unit 2","Interactions Among Branches","Bicameralism (Stimulus)",
     "The Framers created a bicameral legislature to:",
     ["Speed up the legislative process","Provide representation based on both population and state equality while checking legislative power","Give the president more power","Limit judicial review"],1,
     "The two chambers represent different constituencies and check each other."),

    ("Unit 2","Interactions Among Branches","Treaty Power",
     "Treaties negotiated by the president must be approved by:",
     ["A simple majority of the House","A simple majority of the Senate","A two-thirds vote of the Senate","A two-thirds vote of both chambers"],2,
     "The Constitution requires a two-thirds Senate vote to ratify treaties."),

    ("Unit 2","Interactions Among Branches","Recess Appointments",
     "The president can make recess appointments when:",
     ["Congress is in session","The Senate is in recess, temporarily filling vacancies without Senate confirmation","The Supreme Court approves","The House requests it"],1,
     "Recess appointments allow the president to fill positions when the Senate is unavailable."),

    ("Unit 2","Interactions Among Branches","Legislative Riders",
     "A rider attached to a bill is:",
     ["Always relevant to the main bill","An unrelated provision added to a bill likely to pass","Required by the Constitution","Only used in the Senate"],1,
     "Riders allow legislators to advance provisions by attaching them to popular legislation."),

    ("Unit 2","Interactions Among Branches","Bureaucratic Accountability",
     "Which method allows Congress to influence bureaucratic behavior after a law is enacted?",
     ["Only the president can influence agencies","Congressional oversight through hearings, budget control, and reauthorization","Judicial appointments","State government pressure"],1,
     "Congress uses multiple tools to monitor and direct agency implementation."),

    ("Unit 2","Interactions Among Branches","Whistleblower Protections",
     "Whistleblower protection laws encourage government employees to:",
     ["Always agree with their supervisors","Report waste, fraud, and abuse without fear of retaliation","Leak classified information to the press","Ignore problems"],1,
     "These laws protect employees who expose government wrongdoing."),

    ("Unit 2","Interactions Among Branches","Line-Item Veto",
     "The Supreme Court struck down the line-item veto in Clinton v. City of New York because it:",
     ["Was too expensive","Violated the Presentment Clause by allowing the president to unilaterally amend legislation","Was unnecessary","Helped Congress too much"],1,
     "The Court ruled the president cannot selectively cancel parts of enacted legislation."),

    # Unit 3 additions
    ("Unit 3","Civil Liberties and Civil Rights","Establishment Clause Case (Stimulus)",
     "A city places a nativity scene on government property alongside secular holiday decorations. Under the Lemon test, a court would most likely:",
     ["Always strike it down","Allow it because the overall display has a secular purpose","Require a referendum","Ignore the case"],1,
     "Mixed displays with secular elements may pass the Lemon test's secular purpose requirement."),

    ("Unit 3","Civil Liberties and Civil Rights","Free Speech Limits",
     "Which type of speech receives the LEAST First Amendment protection?",
     ["Political speech","Commercial speech","Obscenity","Symbolic speech"],2,
     "Obscenity, as defined by the Miller test, receives no First Amendment protection."),

    ("Unit 3","Civil Liberties and Civil Rights","Commercial Speech",
     "Commercial speech receives:",
     ["No protection","The same protection as political speech","Limited protection — it can be regulated if misleading","Absolute protection"],2,
     "The government can regulate false or misleading advertising, unlike political speech."),

    ("Unit 3","Civil Liberties and Civil Rights","Gitlow v. New York",
     "Gitlow v. New York (1925) was significant because it:",
     ["Ended free speech protections","Began the process of incorporating the Bill of Rights to apply to states through the 14th Amendment","Overturned Marbury v. Madison","Established the exclusionary rule"],1,
     "Gitlow was the first case to apply a Bill of Rights protection to states via the 14th Amendment."),

    ("Unit 3","Civil Liberties and Civil Rights","Korematsu v. United States",
     "Korematsu v. United States (1944) upheld:",
     ["Japanese American internment during World War II","The right to free speech during wartime","School desegregation","The exclusionary rule"],0,
     "The Court allowed internment as a wartime necessity, a decision now widely condemned."),

    ("Unit 3","Civil Liberties and Civil Rights","Shelby County v. Holder",
     "Shelby County v. Holder (2013) struck down a key provision of the Voting Rights Act, which:",
     ["Banned all forms of voter ID","Required certain states to get federal approval before changing voting laws","Eliminated the Electoral College","Established automatic voter registration"],1,
     "The Court invalidated the preclearance formula, weakening federal oversight of voting changes."),

    ("Unit 3","Civil Liberties and Civil Rights","Obergefell v. Hodges",
     "Obergefell v. Hodges (2015) ruled that:",
     ["States can ban same-sex marriage","Same-sex marriage is a constitutional right under the 14th Amendment","Marriage is not a constitutional issue","Only Congress can legalize same-sex marriage"],1,
     "The Court held that the right to marry is guaranteed to same-sex couples."),

    ("Unit 3","Civil Liberties and Civil Rights","Disparate Impact",
     "Disparate impact occurs when:",
     ["A law explicitly discriminates","A facially neutral law or practice disproportionately affects a protected group","Everyone is treated identically","No discrimination exists"],1,
     "Disparate impact looks at outcomes rather than intent."),

    # Unit 4 additions
    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Demographics",
     "Which demographic group has historically been most likely to identify as Democratic?",
     ["White evangelical Christians","African Americans","Rural white voters","Business executives"],1,
     "African Americans have overwhelmingly supported the Democratic Party since the 1960s."),

    ("Unit 4","American Political Ideologies and Beliefs","Media Framing",
     "Media framing refers to:",
     ["Journalists lying about events","How the media presents a story, influencing audience interpretation","Censoring all political content","Reporters running for office"],1,
     "The way a story is framed can shape how the public perceives an issue."),

    ("Unit 4","American Political Ideologies and Beliefs","Agenda Setting",
     "The media's agenda-setting function means it:",
     ["Tells people what to think","Influences what issues people consider important by choosing which stories to cover","Controls government policy","Writes legislation"],1,
     "By selecting stories, the media shapes which issues receive public attention."),

    ("Unit 4","American Political Ideologies and Beliefs","Priming",
     "In media studies, priming refers to:",
     ["Preparing candidates for debates","Media coverage that makes certain issues more prominent in evaluating political figures","Printing newspapers","Polling before elections"],1,
     "Priming influences the criteria people use to judge politicians."),

    ("Unit 4","American Political Ideologies and Beliefs","Selective Exposure",
     "Selective exposure in media consumption means people tend to:",
     ["Watch all news sources equally","Seek out media that reinforces their existing beliefs","Avoid all news","Only read newspapers"],1,
     "People often choose information sources that confirm their pre-existing views."),

    ("Unit 4","American Political Ideologies and Beliefs","Discretionary vs. Mandatory Spending (Stimulus)",
     "A pie chart shows the federal budget with 60% mandatory spending and 30% discretionary spending. The largest component of mandatory spending is most likely:",
     ["Defense","Social Security","Education","NASA"],1,
     "Social Security is the single largest mandatory spending program."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Age",
     "Research generally shows that younger voters tend to be:",
     ["More conservative on social issues","More liberal on social issues than older voters","Identical to older voters","Completely apolitical"],1,
     "Younger generations have tended to be more progressive on social issues."),

    ("Unit 4","American Political Ideologies and Beliefs","Economic Inequality Views",
     "A person who believes the government should do more to reduce income inequality likely holds:",
     ["Conservative views","Liberal views","Libertarian views","No political views"],1,
     "Support for government action to reduce inequality is a core liberal position."),

    # Unit 5 additions
    ("Unit 5","Political Participation","Voter Registration Barriers",
     "Which of the following is NOT a current barrier to voter registration in most states?",
     ["Residency requirements","Registration deadlines before Election Day","Literacy tests","Lack of same-day registration"],2,
     "Literacy tests were banned by the Voting Rights Act of 1965."),

    ("Unit 5","Political Participation","Political Efficacy",
     "Political efficacy refers to:",
     ["The efficiency of government operations","A person's belief that their political participation matters and can influence government","Voter apathy","Government effectiveness"],1,
     "High political efficacy is associated with greater civic participation."),

    ("Unit 5","Political Participation","Incumbency and Fundraising (Stimulus)",
     "Data shows that incumbents raise on average three times more campaign funds than challengers. This primarily occurs because:",
     ["Challengers are not allowed to fundraise","Donors prefer to contribute to incumbents who already have power and influence","The FEC limits challenger fundraising","Incumbents use government funds"],1,
     "Incumbents' existing relationships and influence make them more attractive to donors."),

    ("Unit 5","Political Participation","Proportional Representation",
     "Under a proportional representation system, seats are allocated based on:",
     ["Winner-take-all in each district","The percentage of votes each party receives","Only the top two parties","Random selection"],1,
     "Proportional representation gives parties seats in proportion to their vote share."),

    ("Unit 5","Political Participation","Runoff Elections",
     "A runoff election is held when:",
     ["A candidate wins a majority","No candidate receives the required percentage of votes in the first round","The president requests it","The Supreme Court orders it"],1,
     "Runoffs ensure the eventual winner has broader support."),

    ("Unit 5","Political Participation","Citizens United Impact (Stimulus)",
     "After Citizens United v. FEC (2010), total outside spending in federal elections increased from $338 million in 2008 to over $1 billion in 2012. This data best supports the argument that:",
     ["The decision significantly increased the role of money in politics","Campaign spending decreased","The ruling had no effect","Only individual spending increased"],0,
     "The dramatic increase in outside spending followed directly from the Court's ruling."),

    ("Unit 5","Political Participation","Microtargeting",
     "Microtargeting in political campaigns refers to:",
     ["Advertising to everyone equally","Using data analytics to identify and deliver tailored messages to specific voter segments","Targeting only large cities","Ignoring voter data"],1,
     "Campaigns use voter data to craft personalized outreach to specific demographic groups."),

    ("Unit 5","Political Participation","Party Realignment Example",
     "The election of 1932 is considered a realigning election because:",
     ["Nothing changed","It shifted many voters to the Democratic Party under FDR's New Deal coalition","Republicans gained strength","Third parties won"],1,
     "The Great Depression led to a lasting shift as FDR built a broad Democratic coalition."),

    # Extra cross-unit questions to ensure we hit 500

    ("Unit 1","Foundations of American Democracy","Consent of the Governed",
     "The principle that government derives its authority from the people is called:",
     ["Totalitarianism","Consent of the governed","Aristocracy","Theocracy"],1,
     "Democratic legitimacy depends on the consent of those being governed."),

    ("Unit 1","Foundations of American Democracy","Shays' Rebellion",
     "Shays' Rebellion demonstrated that the Articles of Confederation:",
     ["Were effective at maintaining order","Could not effectively deal with domestic unrest","Gave too much power to the military","Were popular with farmers"],1,
     "The uprising exposed the central government's inability to respond to crises."),

    ("Unit 2","Interactions Among Branches","Impeachment Trial",
     "During a presidential impeachment trial, who presides?",
     ["The Speaker of the House","The Senate Majority Leader","The Vice President","The Chief Justice of the Supreme Court"],3,
     "The Chief Justice presides when the Senate tries a president."),

    ("Unit 2","Interactions Among Branches","Congressional Term Lengths",
     "Members of the House serve terms of how many years?",
     ["Two","Four","Six","Eight"],0,
     "House members serve two-year terms, requiring frequent re-election."),

    ("Unit 2","Interactions Among Branches","Senate Term Length",
     "Senators serve terms of:",
     ["Two years","Four years","Six years","Eight years"],2,
     "Six-year terms give senators more insulation from short-term political pressures."),

    ("Unit 3","Civil Liberties and Civil Rights","Brandenburg v. Ohio",
     "Brandenburg v. Ohio (1969) established that speech can only be restricted if it:",
     ["Is unpopular","Incites imminent lawless action and is likely to produce such action","Offends anyone","Is political in nature"],1,
     "The Brandenburg test is the current standard for when speech can be punished."),

    ("Unit 3","Civil Liberties and Civil Rights","Reasonable Expectation of Privacy",
     "In Katz v. United States (1967), the Court ruled that the Fourth Amendment protects:",
     ["Only physical spaces","People's reasonable expectations of privacy, not just physical places","Government buildings","Public spaces"],1,
     "The ruling expanded Fourth Amendment protections beyond physical trespass."),

    ("Unit 4","American Political Ideologies and Beliefs","Party Coalition Shifts",
     "The ideological shift of the South from Democratic to Republican is an example of:",
     ["Dealignment","Partisan realignment","Third-party dominance","Judicial activism"],1,
     "The Southern realignment shifted conservative white voters to the Republican Party over decades."),

    ("Unit 4","American Political Ideologies and Beliefs","Fiscal Conservative",
     "A fiscal conservative would most likely support:",
     ["Increasing government spending on social programs","Balanced budgets and reduced government spending","Higher taxes on all income levels","Expanding entitlement programs"],1,
     "Fiscal conservatives prioritize lower spending and balanced budgets."),

    ("Unit 5","Political Participation","Voter Turnout Comparison (Stimulus)",
     "U.S. voter turnout (around 60% in presidential years) is lower than many other democracies. Which structural feature most contributes to this?",
     ["Mandatory voting","Voter registration requirements that place the burden on individual citizens","The existence of the Senate","Judicial elections"],1,
     "Unlike many democracies with automatic registration, the U.S. requires individuals to register."),

    ("Unit 5","Political Participation","Grassroots Mobilization",
     "Grassroots mobilization involves:",
     ["Top-down directives from party leaders","Organizing ordinary citizens at the local level to advocate for political change","Only wealthy donors","Government-funded campaigns"],1,
     "Grassroots efforts empower local citizens to participate in the political process."),

    # Fill remaining to reach exactly 500
    ("Unit 1","Foundations of American Democracy","Rule of Law",
     "The rule of law means:",
     ["The president is above the law","Government leaders and citizens are bound by the same laws","Only judges must follow the law","Laws apply differently to each person"],1,
     "No one is above the law in a system governed by the rule of law."),

    ("Unit 2","Interactions Among Branches","Cloture Vote",
     "How many votes are needed to invoke cloture in the Senate?",
     ["51","67","60","75"],2,
     "Sixty senators must vote for cloture to end a filibuster."),

    ("Unit 2","Interactions Among Branches","Markup Session",
     "During a committee markup session, members:",
     ["Debate the bill on the floor","Amend and rewrite the bill line by line","Send the bill to the president","Conduct oversight hearings"],1,
     "Markup is the process where committee members revise legislation in detail."),

    ("Unit 3","Civil Liberties and Civil Rights","Eminent Domain",
     "The Fifth Amendment's Takings Clause requires the government to provide:",
     ["Nothing when taking private property","Just compensation when taking private property for public use","A replacement property","An apology"],1,
     "The government must fairly compensate owners when exercising eminent domain."),

    ("Unit 3","Civil Liberties and Civil Rights","Double Jeopardy",
     "The prohibition against double jeopardy means a person cannot be:",
     ["Tried twice for the same offense by the same sovereign","Arrested without a warrant","Denied bail","Forced to testify against a spouse"],0,
     "The Fifth Amendment protects individuals from being tried twice for the same crime."),

    ("Unit 4","American Political Ideologies and Beliefs","Confirmation Bias",
     "Confirmation bias in political beliefs means people tend to:",
     ["Seek out diverse perspectives","Accept information that confirms their existing views and reject contradictory evidence","Change their minds frequently","Ignore all political news"],1,
     "Confirmation bias reinforces existing beliefs and contributes to political polarization."),

    ("Unit 4","American Political Ideologies and Beliefs","Polarization",
     "Political polarization refers to:",
     ["Everyone agreeing on policy","The growing ideological distance between political parties and their supporters","Reduced voter interest","A third party emerging"],1,
     "Polarization makes compromise more difficult as parties move further apart ideologically."),

    ("Unit 5","Political Participation","Absentee Voting",
     "Absentee voting allows citizens to:",
     ["Vote only if they have a valid excuse","Cast their ballot before Election Day or by mail without being at a polling place","Vote in multiple states","Skip the registration process"],1,
     "Absentee and mail-in voting increase accessibility for those who cannot vote in person."),

    ("Unit 5","Political Participation","Early Voting",
     "Early voting provisions are designed to:",
     ["Discourage voting","Increase voter turnout by providing more convenient voting times","Benefit only one party","Replace Election Day"],1,
     "Early voting reduces barriers by giving people flexibility in when they cast their ballot."),

    ("Unit 1","Foundations of American Democracy","Hobbes State of Nature",
     "Thomas Hobbes described the state of nature as:",
     ["A peaceful paradise","A state of war where life is 'solitary, poor, nasty, brutish, and short'","A democratic society","A constitutional monarchy"],1,
     "Hobbes's bleak view of human nature justified a strong sovereign to maintain order."),

    ("Unit 2","Interactions Among Branches","Power of Oversight (Stimulus)",
     "A congressional committee subpoenas a cabinet secretary to testify about agency spending. This is an example of:",
     ["Judicial review","Executive privilege","Congressional oversight of the bureaucracy","Gerrymandering"],2,
     "Subpoenaing executive officials is a tool of congressional oversight."),

    ("Unit 3","Civil Liberties and Civil Rights","Voting Rights Today (Stimulus)",
     "After Shelby County v. Holder, several states passed new voting restrictions within weeks. Critics argue these laws:",
     ["Expand voting access","Disproportionately affect minority voters, undermining the Voting Rights Act's goals","Have no effect","Only affect federal elections"],1,
     "The removal of preclearance allowed states to enact potentially discriminatory voting changes."),

    ("Unit 4","American Political Ideologies and Beliefs","Values and Ideology",
     "Core American political values include:",
     ["Only individual liberty","Individualism, equality of opportunity, free enterprise, and rule of law","Government control of all aspects of life","Collectivism above individual rights"],1,
     "These shared values form the foundation of American political culture."),

    ("Unit 5","Political Participation","Majority vs. Plurality",
     "In a plurality election, the winner is the candidate who:",
     ["Receives more than 50% of the vote","Receives the most votes, even without a majority","Wins a runoff","Is selected by party leaders"],1,
     "Plurality means the most votes wins, even if it's less than a majority."),

    ("Unit 1","Foundations of American Democracy","Compact Theory",
     "The compact theory of government held that:",
     ["The Constitution was an agreement among the states that they could leave","The federal government created the states","Only the president can interpret the Constitution","Citizens have no rights"],0,
     "This theory, championed by Calhoun, argued states retained ultimate sovereignty."),

    ("Unit 2","Interactions Among Branches","State of the Union",
     "The State of the Union address allows the president to:",
     ["Pass laws","Set the legislative agenda by outlining priorities to Congress and the public","Override Supreme Court decisions","Declare war"],1,
     "The address is a powerful tool for shaping public and congressional attention."),

    ("Unit 3","Civil Liberties and Civil Rights","Loving v. Virginia",
     "Loving v. Virginia (1967) struck down:",
     ["School segregation","Laws banning interracial marriage","Poll taxes","Jim Crow transportation laws"],1,
     "The Court ruled that bans on interracial marriage violated equal protection and due process."),

    ("Unit 4","American Political Ideologies and Beliefs","Political Culture",
     "American political culture is characterized by widespread belief in:",
     ["Aristocratic governance","Democracy, individual rights, and equality of opportunity","One-party rule","Government ownership of all property"],1,
     "Most Americans share core democratic values even when they disagree on specific policies."),

    ("Unit 5","Political Participation","Voter Fatigue",
     "Voter fatigue can occur when:",
     ["Elections are rare","Frequent elections or lengthy ballots lead to decreased participation","Only one candidate runs","Voting is mandatory"],1,
     "Too many elections or complex ballots can lead voters to skip voting altogether."),

    # Additional stimulus questions and variety

    ("Unit 1","Foundations of American Democracy","Federalist vs. Anti-Federalist (Stimulus)",
     "\"A bill of rights is what the people are entitled to against every government on earth.\" — Thomas Jefferson\n\nThis quote most closely aligns with the views of the:",
     ["Federalists","Anti-Federalists","Monarchists","Anarchists"],1,
     "Anti-Federalists and Jefferson insisted on explicit protections for individual rights."),

    ("Unit 2","Interactions Among Branches","Senate Judiciary Committee",
     "The Senate Judiciary Committee plays a critical role in:",
     ["Writing tax legislation","Reviewing and holding hearings on judicial nominations","Overseeing the military","Managing elections"],1,
     "Judicial nominees must pass through the committee before a full Senate vote."),

    ("Unit 3","Civil Liberties and Civil Rights","Regents of UC v. Bakke",
     "In Regents of the University of California v. Bakke (1978), the Court ruled that:",
     ["Racial quotas in university admissions are constitutional","Race can be a factor in admissions but rigid quotas are unconstitutional","Affirmative action is entirely illegal","Only test scores should determine admission"],1,
     "Bakke established that race-conscious admissions are permissible but quotas are not."),

    ("Unit 4","American Political Ideologies and Beliefs","Education and Ideology",
     "Research shows that higher levels of education are associated with:",
     ["Always voting Republican","Always voting Democratic","More liberal views on social issues but varied views on economic issues","No change in political views"],2,
     "Education's effect on political views varies by issue area."),

    ("Unit 5","Political Participation","Voter Mobilization Tactics (Stimulus)",
     "A study shows that personalized text messages reminding voters of their polling location increased turnout by 3%. This demonstrates the effectiveness of:",
     ["Negative campaigning","Targeted voter mobilization efforts using technology","Ignoring voter outreach","Traditional mail campaigns"],1,
     "Modern campaigns use data-driven outreach methods to boost participation."),

    # Final batch to reach 500

    ("Unit 1","Foundations of American Democracy","Separation of Powers Purpose",
     "The purpose of separating powers among three branches is to:",
     ["Make government more efficient","Prevent any one branch from becoming too powerful","Give the president supreme authority","Eliminate the need for elections"],1,
     "Separation of powers distributes authority to prevent tyranny."),

    ("Unit 2","Interactions Among Branches","Rule of Four",
     "The 'Rule of Four' at the Supreme Court means:",
     ["Four justices must agree to hear a case for certiorari to be granted","Four branches of government exist","Cases need four hearings","Four amendments apply"],0,
     "At least four justices must vote to accept a case for the Court to grant review."),

    ("Unit 2","Interactions Among Branches","Amicus Curiae",
     "An amicus curiae brief is filed by:",
     ["The defendant only","The prosecution only","A third party not directly involved in the case who has an interest in the outcome","The jury"],2,
     "Interest groups and other parties file amicus briefs to influence court decisions."),

    ("Unit 3","Civil Liberties and Civil Rights","Habeas Corpus",
     "A writ of habeas corpus protects against:",
     ["Unreasonable searches","Unlawful detention by requiring authorities to justify holding a person","Self-incrimination","Excessive bail"],1,
     "Habeas corpus ensures that no one is imprisoned without legal cause."),

    ("Unit 3","Civil Liberties and Civil Rights","Equal Rights Amendment",
     "The Equal Rights Amendment was proposed but never ratified. It would have:",
     ["Abolished the Electoral College","Guaranteed equal rights regardless of sex","Lowered the voting age to 16","Established term limits for Congress"],1,
     "The ERA fell short of the required state ratifications before its deadline."),

    ("Unit 4","American Political Ideologies and Beliefs","Religious Right",
     "The Religious Right movement in American politics primarily supports:",
     ["Separation of church and state","Social conservative policies aligned with evangelical Christian values","Liberal economic policy","Reduced military spending"],1,
     "The Religious Right has been a powerful force within the Republican Party since the 1980s."),

    ("Unit 4","American Political Ideologies and Beliefs","Blue Dog Democrats",
     "Blue Dog Democrats are typically:",
     ["Very liberal","Moderate to conservative Democrats often from competitive districts","Socialists","Identical to progressive Democrats"],1,
     "Blue Dogs are centrist Democrats who often break with their party on fiscal or social issues."),

    ("Unit 5","Political Participation","Voter Age and Turnout",
     "Which age group consistently has the LOWEST voter turnout?",
     ["18–29 year olds","30–44 year olds","45–64 year olds","65 and older"],0,
     "Young voters have historically had the lowest participation rates."),

    ("Unit 5","Political Participation","Partisan Primary Effects",
     "Critics argue that closed primaries can lead to:",
     ["More moderate candidates","More ideologically extreme nominees because only party loyalists vote","Higher turnout","Fewer candidates running"],1,
     "When only strong partisans vote, candidates may appeal to the base rather than the center."),

    ("Unit 1","Foundations of American Democracy","Social Contract Details",
     "In social contract theory, people agree to give up some freedoms in exchange for:",
     ["Government protection and order","Absolute liberty","No government at all","Corporate profits"],0,
     "The social contract involves trading some natural freedom for security and organized governance."),

    ("Unit 2","Interactions Among Branches","Congressional Budget Process",
     "The federal budget process begins when:",
     ["Congress writes its own budget from scratch","The president submits a budget proposal to Congress","The Supreme Court allocates funds","State governors set the budget"],1,
     "The president's budget proposal starts the process, but Congress has the power of the purse."),

    ("Unit 3","Civil Liberties and Civil Rights","Gonzalez v. Carhart",
     "In Gonzalez v. Carhart (2007), the Court upheld:",
     ["Unrestricted abortion rights","A federal ban on a specific late-term abortion procedure","Complete state control over abortion","The original Roe v. Wade framework"],1,
     "The ruling upheld the Partial-Birth Abortion Ban Act."),

    ("Unit 4","American Political Ideologies and Beliefs","Moderate Voters",
     "Moderate voters are important in elections because they:",
     ["Always vote for incumbents","Can swing elections since they are not firmly committed to either party","Never vote","Only vote in midterms"],1,
     "Moderates are often the decisive voters in competitive elections."),

    ("Unit 5","Political Participation","Super Tuesday",
     "Super Tuesday is significant because:",
     ["It is the final day of primary elections","Many states hold primaries on the same day, often determining the nominee","It is a federal holiday","Only superdelegates vote on this day"],1,
     "The large number of simultaneous primaries can effectively decide the nomination."),

    # ── Additional questions to reach 500 ──

    # UNIT 1 additions (36 more → total 100)
    ("Unit 1","Foundations of American Democracy","Popular Sovereignty",
     "Popular sovereignty means that government power comes from:",
     ["The military","The consent of the governed","The Constitution alone","Religious authority"],1,
     "Popular sovereignty holds that the people are the ultimate source of government authority."),

    ("Unit 1","Foundations of American Democracy","Limited Government",
     "The concept of limited government is best described as:",
     ["Government has no power","Government power is restricted by law","Only the president has power","States have no authority"],1,
     "Limited government means the government can only exercise powers granted to it by the people through law."),

    ("Unit 1","Foundations of American Democracy","Rule of Law",
     "The rule of law means that:",
     ["The president is above the law","Laws apply equally to all, including government officials","Judges make all laws","Only Congress must follow the law"],1,
     "The rule of law ensures that no person or institution is above the law."),

    ("Unit 1","Foundations of American Democracy","Natural Rights",
     "According to John Locke, natural rights include:",
     ["Life, liberty, and the pursuit of happiness","Life, liberty, and property","Speech, press, and assembly","Voting, petition, and protest"],1,
     "Locke identified life, liberty, and property as fundamental natural rights."),

    ("Unit 1","Foundations of American Democracy","Social Contract",
     "The social contract theory suggests that:",
     ["Government is divinely ordained","People agree to give up some freedom in exchange for protection","The strongest should rule","Democracy is the only legitimate government"],1,
     "Social contract theory holds that government legitimacy comes from the consent of the governed."),

    ("Unit 1","Foundations of American Democracy","Participatory Democracy",
     "Participatory democracy emphasizes:",
     ["Elite decision-making","Broad citizen involvement in political processes","Military rule","Corporate governance"],1,
     "Participatory democracy stresses active citizen engagement in government decisions."),

    ("Unit 1","Foundations of American Democracy","Pluralist Democracy",
     "Pluralist democracy theory argues that:",
     ["One group dominates politics","Power is distributed among many competing groups","Only elites make decisions","Direct democracy is best"],1,
     "Pluralism holds that multiple groups compete for influence, preventing any single group from dominating."),

    ("Unit 1","Foundations of American Democracy","Elite Democracy",
     "Elite democracy theory holds that:",
     ["All citizens participate equally","A small group of wealthy and well-educated citizens lead government","Direct voting on all issues is best","Political parties are unnecessary"],1,
     "Elite theory suggests that a small minority of wealthy, educated people make most political decisions."),

    ("Unit 1","Foundations of American Democracy","Ratification Debates",
     "The main debate during ratification of the Constitution was between:",
     ["Democrats and Republicans","Federalists and Anti-Federalists","Northern and Southern states only","Congress and the president"],1,
     "Federalists supported the Constitution while Anti-Federalists opposed it without a Bill of Rights."),

    ("Unit 1","Foundations of American Democracy","Bill of Rights Purpose",
     "The Bill of Rights was added to the Constitution primarily to:",
     ["Create the federal court system","Protect individual liberties from government overreach","Establish the Electoral College","Define presidential powers"],1,
     "The first ten amendments protect fundamental rights and were added to address Anti-Federalist concerns."),

    ("Unit 1","Foundations of American Democracy","Federalist No. 70",
     "In Federalist No. 70, Alexander Hamilton argues for:",
     ["A weak executive","A strong, unitary executive","Congressional supremacy","Direct democracy"],1,
     "Hamilton argued that 'energy in the executive' requires a single president with decisive authority."),

    ("Unit 1","Foundations of American Democracy","Cooperative Federalism",
     "Cooperative federalism is characterized by:",
     ["Strict separation of state and federal powers","National and state governments working together on shared programs","Complete federal dominance","States acting independently of the federal government"],1,
     "Cooperative federalism involves collaboration between levels of government, often called 'marble-cake' federalism."),

    ("Unit 1","Foundations of American Democracy","Dual Federalism",
     "Dual federalism is best described as:",
     ["Overlapping responsibilities between state and federal government","A clear division of authority between state and federal governments","Complete federal control","States ignoring federal law"],1,
     "Dual federalism, or 'layer-cake' federalism, maintains distinct spheres of authority for each level."),

    ("Unit 1","Foundations of American Democracy","Fiscal Federalism",
     "Fiscal federalism refers to:",
     ["State taxation only","The system of federal grants and funding to state and local governments","The national debt","Congressional budget process"],1,
     "Fiscal federalism describes how the federal government uses grants to influence state policy."),

    ("Unit 1","Foundations of American Democracy","Block Grants",
     "Block grants differ from categorical grants because they:",
     ["Must be used for specific purposes","Give states broad discretion in how to spend the funds","Come from state governments","Require no matching funds"],1,
     "Block grants provide funds with fewer restrictions, giving states flexibility in spending."),

    ("Unit 1","Foundations of American Democracy","Unfunded Mandates",
     "Unfunded mandates are controversial because they:",
     ["Give states too much money","Require states to implement federal policies without federal funding","Allow states to ignore federal law","Only apply to large states"],1,
     "Unfunded mandates impose costs on states without providing financial support."),

    ("Unit 1","Foundations of American Democracy","10th Amendment",
     "The 10th Amendment reserves powers to:",
     ["The federal government","The states or the people","The president","The Supreme Court"],1,
     "The 10th Amendment states that powers not delegated to the federal government are reserved to the states or the people."),

    ("Unit 1","Foundations of American Democracy","Privileges and Immunities",
     "The Privileges and Immunities Clause requires states to:",
     ["Give their citizens extra rights","Treat citizens of other states fairly and equally","Allow free travel only","Share tax revenue"],1,
     "States cannot discriminate against citizens of other states regarding fundamental rights."),

    ("Unit 1","Foundations of American Democracy","Devolution",
     "Devolution refers to:",
     ["Increasing federal power","Transferring power from the federal government to state governments","Eliminating state governments","Judicial activism"],1,
     "Devolution is the process of shifting responsibilities from the federal level to the states."),

    ("Unit 1","Foundations of American Democracy","Categorical Grants",
     "Categorical grants require state governments to:",
     ["Spend money however they choose","Use funds for specific, federally defined purposes","Match no funding","Apply through their governors only"],1,
     "Categorical grants come with strict conditions on how the money must be spent."),

    ("Unit 1","Foundations of American Democracy","Marbury v. Madison",
     "Marbury v. Madison is significant because it established:",
     ["The right to vote","The power of judicial review","Presidential term limits","Congressional oversight"],1,
     "Chief Justice Marshall's ruling established the Supreme Court's authority to declare laws unconstitutional."),

    ("Unit 1","Foundations of American Democracy","Necessary and Proper Clause Impact",
     "The Necessary and Proper Clause has been used to:",
     ["Limit federal power","Expand Congress's authority beyond enumerated powers","Give states more autonomy","Reduce presidential authority"],1,
     "The Elastic Clause allows Congress to pass laws beyond those specifically listed in Article I."),

    ("Unit 1","Foundations of American Democracy","Article V",
     "Article V of the Constitution describes the process for:",
     ["Electing the president","Amending the Constitution","Creating federal courts","Declaring war"],1,
     "Article V outlines two methods for proposing and ratifying constitutional amendments."),

    ("Unit 1","Foundations of American Democracy","Separation of Powers Purpose",
     "The primary purpose of separation of powers is to:",
     ["Make government more efficient","Prevent the concentration of power in any single branch","Give the president more authority","Allow states to override federal law"],1,
     "Dividing power among branches prevents tyranny by ensuring no single branch dominates."),

    ("Unit 1","Foundations of American Democracy","Federalist No. 78",
     "In Federalist No. 78, Hamilton argues that the judiciary is the 'least dangerous branch' because it:",
     ["Controls the military","Has neither the power of the purse nor the sword","Is elected by the people","Can override Congress"],1,
     "Hamilton noted that courts depend on the executive to enforce decisions and Congress for funding."),

    ("Unit 1","Foundations of American Democracy","Consent of the Governed",
     "The idea of 'consent of the governed' is central to:",
     ["Authoritarian government","Democratic legitimacy and the Declaration of Independence","Monarchy","Theocracy"],1,
     "The Declaration states that governments derive their just powers from the consent of the governed."),

    ("Unit 1","Foundations of American Democracy","Republican Government",
     "The Founders chose a republican form of government because they:",
     ["Wanted direct democracy","Believed elected representatives would filter popular passions","Opposed all forms of voting","Wanted monarchy"],1,
     "The Founders feared pure democracy and chose representative government to temper majority factions."),

    ("Unit 1","Foundations of American Democracy","Interstate Compact Clause",
     "The Interstate Compact Clause requires that agreements between states:",
     ["Never occur","Receive congressional approval","Be approved by the president only","Be ratified by all 50 states"],1,
     "States may enter into compacts with each other, but significant agreements require congressional consent."),

    ("Unit 1","Foundations of American Democracy","Extradition Clause",
     "The Extradition Clause requires that:",
     ["States can refuse to return fugitives","A state must return a person accused of a crime to the state where the crime occurred","Only the federal government handles fugitives","International treaties govern all extraditions"],1,
     "Article IV requires states to return fugitives to the state where they are charged."),

    ("Unit 1","Foundations of American Democracy","Shays Rebellion",
     "Shays' Rebellion demonstrated the need for:",
     ["Weaker federal government","A stronger national government that could maintain order","More state sovereignty","Abolishing the military"],1,
     "The uprising of indebted farmers exposed the weakness of the Articles of Confederation."),

    ("Unit 1","Foundations of American Democracy","Virginia Plan vs New Jersey Plan",
     "The Virginia Plan proposed representation based on:",
     ["Equal representation for all states","State population size","Geographic area","Wealth of each state"],1,
     "Larger states favored the Virginia Plan's population-based representation in both chambers."),

    ("Unit 1","Foundations of American Democracy","Electoral College Purpose",
     "The Electoral College was created as a compromise between:",
     ["Northern and Southern states","Election by Congress and election by popular vote","Large and small states only","Federalists and Anti-Federalists only"],1,
     "The Founders designed the Electoral College as a middle ground between congressional and popular election."),

    ("Unit 1","Foundations of American Democracy","Three-Fifths Compromise",
     "The Three-Fifths Compromise addressed:",
     ["How states would be represented in the Senate","How enslaved persons would be counted for representation and taxation","Tariffs on imported goods","The slave trade"],1,
     "Enslaved individuals were counted as three-fifths of a person for apportionment purposes."),

    ("Unit 1","Foundations of American Democracy","Implied Powers",
     "Implied powers of Congress are those that:",
     ["Are explicitly listed in the Constitution","Are reasonably inferred from enumerated powers through the Necessary and Proper Clause","Belong only to the states","Are granted by the president"],1,
     "Implied powers allow Congress flexibility to address issues not explicitly covered in the Constitution."),

    ("Unit 1","Foundations of American Democracy","Mandates in Federalism",
     "Federal mandates can affect state policy by:",
     ["Having no impact on states","Requiring states to comply with federal standards as a condition of receiving funds","Letting states completely ignore federal law","Only applying to border states"],1,
     "The federal government uses mandates and conditions on grants to influence state behavior."),

    ("Unit 1","Foundations of American Democracy","Supremacy Clause Application",
     "When a state law conflicts with a valid federal law, the Supremacy Clause dictates that:",
     ["The state law prevails","The federal law prevails","Both are void","The Supreme Court decides case-by-case"],1,
     "Article VI establishes that federal law is the supreme law of the land when there is a conflict."),

    # UNIT 2 additions (34 more → total 100)
    ("Unit 2","Interactions Among Branches","Executive Agreements",
     "Executive agreements differ from treaties because they:",
     ["Require Senate approval","Do not require Senate ratification","Must be approved by the House","Cannot involve foreign nations"],1,
     "Presidents use executive agreements to make deals with foreign leaders without Senate consent."),

    ("Unit 2","Interactions Among Branches","Judicial Activism",
     "Judicial activism occurs when judges:",
     ["Strictly follow precedent","Interpret the Constitution broadly to shape social policy","Refuse to hear cases","Defer to the legislature on all matters"],1,
     "Activist judges are willing to strike down laws and issue broad rulings on policy questions."),

    ("Unit 2","Interactions Among Branches","Judicial Restraint",
     "Judicial restraint is the philosophy that courts should:",
     ["Actively create new rights","Defer to elected branches and avoid overturning laws unless clearly unconstitutional","Always side with the government","Ignore precedent"],1,
     "Proponents of restraint argue that courts should respect the democratic process."),

    ("Unit 2","Interactions Among Branches","Rule of Four",
     "The 'Rule of Four' in the Supreme Court refers to:",
     ["Four justices must recuse themselves","Four justices must agree to hear a case for certiorari to be granted","A case must have four appeals","Four amicus briefs are required"],1,
     "At least four of the nine justices must vote to grant certiorari for the Court to hear a case."),

    ("Unit 2","Interactions Among Branches","Amicus Curiae",
     "An amicus curiae brief is filed by:",
     ["The defendant only","A non-party with an interest in the case to provide additional perspective","The judge","The jury"],1,
     "Amicus ('friend of the court') briefs allow outside groups to influence the Court's reasoning."),

    ("Unit 2","Interactions Among Branches","Majority Opinion",
     "A majority opinion is significant because it:",
     ["Has no legal effect","Establishes binding legal precedent","Only applies to the specific parties","Is written by the losing side"],1,
     "The majority opinion represents the Court's official ruling and becomes the law of the land."),

    ("Unit 2","Interactions Among Branches","Dissenting Opinion",
     "A dissenting opinion in a Supreme Court case:",
     ["Becomes law","Is written by justices who disagree with the majority and may influence future rulings","Is always unanimous","Must be signed by all justices"],1,
     "Dissents can lay the groundwork for future cases to overturn the majority's precedent."),

    ("Unit 2","Interactions Among Branches","Concurring Opinion",
     "A concurring opinion agrees with the majority ruling but:",
     ["For the same reasons","For different legal reasoning","Disagrees with the outcome","Is written by the losing party"],1,
     "Concurrences allow justices to express alternative rationales for reaching the same conclusion."),

    ("Unit 2","Interactions Among Branches","Pocket Veto",
     "A pocket veto occurs when:",
     ["The president vetoes a bill publicly","The president takes no action on a bill and Congress adjourns within 10 days","Congress overrides a veto","The vice president vetoes a bill"],1,
     "If the president does not sign a bill and Congress adjourns during the 10-day window, the bill dies."),

    ("Unit 2","Interactions Among Branches","Line Item Veto",
     "The Supreme Court struck down the line-item veto because it:",
     ["Was too expensive","Violated the Presentment Clause by allowing the president to amend legislation","Was never used","Gave Congress too much power"],1,
     "In Clinton v. City of New York (1998), the Court ruled the line-item veto unconstitutional."),

    ("Unit 2","Interactions Among Branches","Discharge Petition",
     "A discharge petition in the House is used to:",
     ["Fire a committee chair","Force a bill out of committee to the full floor for a vote","Override a veto","Impeach a president"],1,
     "A majority (218) of House members must sign a discharge petition to bring a bill to the floor."),

    ("Unit 2","Interactions Among Branches","Riders and Amendments",
     "A rider in legislation is:",
     ["A mandatory provision","An unrelated amendment attached to a bill to gain passage","A veto by the president","A filibuster tactic"],1,
     "Riders are provisions added to must-pass bills that might not pass on their own merits."),

    ("Unit 2","Interactions Among Branches","Government Corporations",
     "Government corporations like the U.S. Postal Service differ from agencies because they:",
     ["Have no employees","Operate more like businesses and can charge for services","Are completely private","Report to state governments"],1,
     "Government corporations provide services that could be offered by the private sector."),

    ("Unit 2","Interactions Among Branches","Independent Executive Agencies",
     "Independent executive agencies report to:",
     ["Congress directly","The president but are not part of cabinet departments","The Supreme Court","State governors"],1,
     "Agencies like NASA and the EPA operate independently of cabinet departments but answer to the president."),

    ("Unit 2","Interactions Among Branches","Iron Triangle Dynamics",
     "An iron triangle creates policy through the relationship between:",
     ["Three branches of government","A congressional committee, a bureaucratic agency, and an interest group","Three political parties","Federal, state, and local courts"],1,
     "These three actors form a mutually beneficial relationship to influence policy in a specific area."),

    ("Unit 2","Interactions Among Branches","Issue Networks",
     "Issue networks differ from iron triangles because they:",
     ["Are permanent and closed","Include a broader, more fluid group of participants on a policy issue","Have fewer members","Only involve the president"],1,
     "Issue networks are more open and include experts, media, and various interest groups."),

    ("Unit 2","Interactions Among Branches","Bureaucratic Discretion",
     "Bureaucratic discretion refers to:",
     ["Strict rule-following with no flexibility","The latitude agencies have in interpreting and implementing laws","The president's veto power","Congressional oversight"],1,
     "Agencies often must interpret vague legislation, giving unelected officials significant policy influence."),

    ("Unit 2","Interactions Among Branches","Congressional Budget Process",
     "The federal budget process begins when:",
     ["Congress writes its own budget","The president submits a budget proposal to Congress","The Supreme Court sets spending limits","State governors submit requests"],1,
     "The president's budget proposal is the starting point, though Congress has the final say on spending."),

    ("Unit 2","Interactions Among Branches","Confirmation Hearings",
     "Senate confirmation hearings for judicial nominees have become more contentious because:",
     ["The Constitution requires it","Federal judges serve life terms, making appointments high-stakes ideological battles","Nominees are elected by the public","The House also confirms judges"],1,
     "Lifetime appointments mean each justice can shape law for decades, intensifying partisan conflict."),

    ("Unit 2","Interactions Among Branches","Executive Privilege",
     "Executive privilege is the president's claimed right to:",
     ["Ignore Supreme Court rulings","Withhold information from Congress and the courts to protect national security","Pardon any crime","Declare war without Congress"],1,
     "While not explicitly in the Constitution, courts have recognized limited executive privilege."),

    ("Unit 2","Interactions Among Branches","Recess Appointments",
     "Recess appointments allow the president to:",
     ["Fire members of Congress","Temporarily fill vacancies when the Senate is in recess without confirmation","Adjourn Congress","Override a veto"],1,
     "Recess appointments bypass Senate confirmation but expire at the end of the next Senate session."),

    ("Unit 2","Interactions Among Branches","Delegated Legislation",
     "When Congress delegates rulemaking authority to agencies, this is called:",
     ["Judicial review","Delegated or administrative rulemaking","Impeachment","Cloture"],1,
     "Congress often passes broad statutes and lets agencies fill in the details through regulations."),

    ("Unit 2","Interactions Among Branches","Whistleblower Protections",
     "Whistleblower protections are important because they:",
     ["Punish government employees","Encourage reporting of government waste and abuse by protecting employees from retaliation","Allow agencies to ignore Congress","Eliminate bureaucratic discretion"],1,
     "These protections help ensure government accountability by shielding those who report wrongdoing."),

    ("Unit 2","Interactions Among Branches","Power of Impeachment",
     "The standard for impeachment is:",
     ["Criminal conviction","High crimes and misdemeanors, as determined by Congress","Losing a popular vote","Unpopularity in polls"],1,
     "The Constitution gives Congress broad discretion to define impeachable offenses."),

    ("Unit 2","Interactions Among Branches","Treaty Power",
     "The president negotiates treaties, but they must be ratified by:",
     ["A simple majority of the House","A two-thirds vote of the Senate","A popular referendum","The Supreme Court"],1,
     "Article II requires a two-thirds Senate supermajority to ratify treaties."),

    ("Unit 2","Interactions Among Branches","Senatorial Courtesy",
     "Senatorial courtesy is the practice of:",
     ["Always confirming nominees","The president consulting with home-state senators before nominating federal judges","Senators never opposing each other","Automatic approval of all appointments"],1,
     "This informal practice gives senators influence over judicial appointments in their states."),

    ("Unit 2","Interactions Among Branches","Holds in the Senate",
     "A Senate hold allows a single senator to:",
     ["Pass a bill immediately","Delay or block consideration of a bill or nomination","Override the president","Dismiss a committee chair"],1,
     "Holds are an informal practice that can be used to leverage negotiations or block action."),

    ("Unit 2","Interactions Among Branches","Omnibus Legislation",
     "Omnibus bills are significant because they:",
     ["Address only one narrow issue","Combine many provisions into a single large bill, making them harder to oppose","Are always vetoed","Only deal with the budget"],1,
     "Omnibus legislation bundles multiple policies together, often as a strategy to pass controversial provisions."),

    ("Unit 2","Interactions Among Branches","Continuing Resolution",
     "When Congress cannot pass a budget on time, it may pass a continuing resolution which:",
     ["Shuts down the government","Funds the government at current levels temporarily","Increases all spending","Eliminates the national debt"],1,
     "Continuing resolutions maintain existing funding levels while Congress negotiates a new budget."),

    ("Unit 2","Interactions Among Branches","Government Shutdown",
     "A government shutdown occurs when:",
     ["The president resigns","Congress fails to pass appropriations bills or a continuing resolution","The Supreme Court orders it","A natural disaster strikes"],1,
     "Without funding legislation, non-essential government operations must cease."),

    ("Unit 2","Interactions Among Branches","Presentment Clause",
     "The Presentment Clause requires that:",
     ["The president present a State of the Union address","Every bill passed by Congress must be presented to the president for signature or veto","Judges present opinions to Congress","Citizens present petitions"],1,
     "This clause ensures the president has the opportunity to approve or reject legislation."),

    ("Unit 2","Interactions Among Branches","22nd Amendment",
     "The 22nd Amendment limits the president to:",
     ["One term","Two terms in office","Three terms","Unlimited terms"],1,
     "Ratified in 1951 after FDR served four terms, it limits presidents to two elected terms."),

    ("Unit 2","Interactions Among Branches","25th Amendment",
     "The 25th Amendment addresses:",
     ["Voting rights","Presidential succession and disability","Freedom of speech","States' rights"],1,
     "It clarifies the process when a president is unable to serve and how vacancies are filled."),

    ("Unit 2","Interactions Among Branches","Bureaucratic Accountability",
     "Congress checks bureaucratic power through all of the following EXCEPT:",
     ["Hearings and investigations","Controlling agency budgets","Issuing executive orders to agencies","Rewriting enabling legislation"],2,
     "Executive orders are a presidential tool; Congress uses oversight hearings, budgets, and legislation."),

    # UNIT 3 additions (37 more → total 100)
    ("Unit 3","Civil Liberties and Civil Rights","Free Exercise Clause",
     "The Free Exercise Clause protects:",
     ["Government establishment of religion","The right of individuals to practice their religion freely","Only Christian worship","Prayer in public schools"],1,
     "The First Amendment protects religious practice, though the government may impose neutral, generally applicable laws."),

    ("Unit 3","Civil Liberties and Civil Rights","Lemon Test",
     "The Lemon test, from Lemon v. Kurtzman, evaluates whether a government action:",
     ["Violates free speech","Violates the Establishment Clause by lacking a secular purpose or excessively entangling government with religion","Is a valid tax","Protects property rights"],1,
     "The three-pronged test assesses secular purpose, primary effect, and excessive entanglement."),

    ("Unit 3","Civil Liberties and Civil Rights","Symbolic Speech",
     "In Texas v. Johnson, the Supreme Court ruled that flag burning is:",
     ["Always illegal","Protected symbolic speech under the First Amendment","Only legal in wartime","A form of treason"],1,
     "The Court held that flag burning is expressive conduct protected by the First Amendment."),

    ("Unit 3","Civil Liberties and Civil Rights","Prior Restraint",
     "Prior restraint refers to government action that:",
     ["Punishes speech after the fact","Prevents expression before it occurs, which is presumptively unconstitutional","Protects speech","Encourages more speech"],1,
     "Near v. Minnesota and the Pentagon Papers case established strong protections against prior restraint."),

    ("Unit 3","Civil Liberties and Civil Rights","Obscenity Standard",
     "The Miller test determines whether material is obscene based on:",
     ["Any offensiveness","Community standards, whether it appeals to prurient interest, and whether it lacks serious value","Government opinion","Popular vote"],1,
     "Miller v. California established a three-part test for obscenity, which is not protected speech."),

    ("Unit 3","Civil Liberties and Civil Rights","Commercial Speech",
     "Commercial speech receives:",
     ["No protection","Some First Amendment protection, but less than political speech","Full protection equal to political speech","More protection than political speech"],1,
     "The government can regulate advertising more than political expression but cannot ban truthful ads."),

    ("Unit 3","Civil Liberties and Civil Rights","Libel and Slander",
     "Public officials suing for libel must prove:",
     ["Simple negligence","Actual malice—that the statement was made with knowledge of its falsity or reckless disregard","Any inaccuracy","That they were offended"],1,
     "New York Times v. Sullivan set a high bar for public figures to win defamation cases."),

    ("Unit 3","Civil Liberties and Civil Rights","Right to Privacy",
     "The right to privacy is:",
     ["Explicitly stated in the Bill of Rights","Implied from several amendments including the 1st, 3rd, 4th, 5th, and 14th","Only in the 4th Amendment","Not recognized by courts"],1,
     "Griswold v. Connecticut found a right to privacy in the 'penumbras' of various amendments."),

    ("Unit 3","Civil Liberties and Civil Rights","Exclusionary Rule Origin",
     "The exclusionary rule was applied to states through:",
     ["The 5th Amendment directly","Mapp v. Ohio, incorporating the 4th Amendment via the 14th","A congressional statute","Executive order"],1,
     "Mapp extended the federal exclusionary rule to state courts through selective incorporation."),

    ("Unit 3","Civil Liberties and Civil Rights","Right to Counsel",
     "The right to counsel in state criminal cases was established by:",
     ["Miranda v. Arizona","Gideon v. Wainwright, which incorporated the 6th Amendment right to an attorney","Marbury v. Madison","Brown v. Board"],1,
     "Gideon held that states must provide lawyers for defendants who cannot afford them."),

    ("Unit 3","Civil Liberties and Civil Rights","Double Jeopardy",
     "The protection against double jeopardy means:",
     ["You can be tried twice for the same crime","A person cannot be tried twice for the same offense by the same government","You cannot appeal a conviction","All charges must be filed at once"],1,
     "The 5th Amendment protects against being tried twice, though separate sovereigns (state and federal) may both prosecute."),

    ("Unit 3","Civil Liberties and Civil Rights","Cruel and Unusual Punishment",
     "The 8th Amendment's prohibition on cruel and unusual punishment has been interpreted to:",
     ["Allow any punishment","Evolve with society's standards of decency","Apply only to physical punishment","Never change"],1,
     "The Court uses 'evolving standards of decency' to determine what punishments are prohibited."),

    ("Unit 3","Civil Liberties and Civil Rights","Death Penalty Jurisprudence",
     "The Supreme Court has ruled that the death penalty:",
     ["Is always unconstitutional","Is constitutional but cannot be applied to juveniles or intellectually disabled defendants","Must be mandatory for murder","Can be imposed for any felony"],1,
     "Roper v. Simmons banned execution of juveniles; Atkins v. Virginia banned it for the intellectually disabled."),

    ("Unit 3","Civil Liberties and Civil Rights","Strict Scrutiny",
     "Strict scrutiny is the standard of review used when government action involves:",
     ["Economic regulation","A suspect classification like race or a fundamental right","Traffic laws","Property taxes"],1,
     "Under strict scrutiny, the government must show a compelling interest and the law must be narrowly tailored."),

    ("Unit 3","Civil Liberties and Civil Rights","Intermediate Scrutiny",
     "Intermediate scrutiny applies to classifications based on:",
     ["Race","Gender, requiring the government to show an important interest","Wealth","Age"],1,
     "Craig v. Boren established intermediate scrutiny for gender-based classifications."),

    ("Unit 3","Civil Liberties and Civil Rights","Rational Basis Test",
     "The rational basis test requires that a law:",
     ["Serve a compelling interest","Be rationally related to a legitimate government interest","Pass strict scrutiny","Be approved by voters"],1,
     "This is the most deferential standard; most economic and social legislation passes this test."),

    ("Unit 3","Civil Liberties and Civil Rights","Voting Rights Act Provisions",
     "The Voting Rights Act of 1965 was strengthened by:",
     ["Eliminating all voting requirements","Requiring federal preclearance of voting changes in jurisdictions with histories of discrimination","Allowing only federal elections","Banning political parties"],1,
     "Section 5 preclearance was a key enforcement mechanism until Shelby County v. Holder (2013)."),

    ("Unit 3","Civil Liberties and Civil Rights","Shelby County v. Holder",
     "In Shelby County v. Holder (2013), the Supreme Court:",
     ["Strengthened the VRA","Struck down the coverage formula used to determine which jurisdictions needed preclearance","Banned all voter ID laws","Extended voting rights to non-citizens"],1,
     "The ruling effectively ended federal preclearance, leaving it to Congress to update the formula."),

    ("Unit 3","Civil Liberties and Civil Rights","Affirmative Action History",
     "Affirmative action policies were originally designed to:",
     ["Discriminate against white applicants","Address historical discrimination by promoting opportunities for minorities and women","Eliminate all standardized testing","Guarantee equal outcomes"],1,
     "Affirmative action aimed to remedy past discrimination and promote diversity."),

    ("Unit 3","Civil Liberties and Civil Rights","Title IX",
     "Title IX of the Education Amendments of 1972 prohibits:",
     ["Racial discrimination in voting","Sex-based discrimination in federally funded educational programs","Age discrimination in employment","Religious discrimination in housing"],1,
     "Title IX has been influential in expanding women's athletics and addressing sexual harassment in schools."),

    ("Unit 3","Civil Liberties and Civil Rights","Americans with Disabilities Act",
     "The Americans with Disabilities Act (1990) requires:",
     ["Nothing of private businesses","Reasonable accommodations for people with disabilities in employment and public spaces","Free healthcare for all disabled persons","Special voting procedures"],1,
     "The ADA prohibits discrimination and mandates accessibility in workplaces and public facilities."),

    ("Unit 3","Civil Liberties and Civil Rights","13th Amendment",
     "The 13th Amendment accomplished:",
     ["Women's suffrage","The abolition of slavery and involuntary servitude","Lowering the voting age","Establishing Prohibition"],1,
     "Ratified in 1865, the 13th Amendment permanently ended slavery in the United States."),

    ("Unit 3","Civil Liberties and Civil Rights","15th Amendment Purpose",
     "The 15th Amendment was designed to:",
     ["Give women the right to vote","Prohibit denial of voting rights based on race, color, or previous condition of servitude","Abolish slavery","Establish equal protection"],1,
     "Despite the amendment, Southern states used poll taxes and literacy tests to circumvent it for decades."),

    ("Unit 3","Civil Liberties and Civil Rights","19th Amendment Impact",
     "The 19th Amendment significantly expanded democracy by:",
     ["Lowering the voting age","Granting women the right to vote in all elections","Abolishing poll taxes","Establishing direct election of senators"],1,
     "Ratified in 1920, it doubled the potential electorate by enfranchising women."),

    ("Unit 3","Civil Liberties and Civil Rights","24th Amendment",
     "The 24th Amendment eliminated:",
     ["The Electoral College","Poll taxes in federal elections","Term limits","Slavery"],1,
     "Poll taxes had been used primarily in the South to disenfranchise African American voters."),

    ("Unit 3","Civil Liberties and Civil Rights","Civil Rights Movement Strategy",
     "The civil rights movement achieved its goals primarily through:",
     ["Armed revolution","Nonviolent protest, litigation, and legislative lobbying","Secession threats","Third-party politics"],1,
     "Leaders like MLK Jr. used civil disobedience, legal challenges, and political pressure."),

    ("Unit 3","Civil Liberties and Civil Rights","De Facto vs De Jure Segregation",
     "De facto segregation differs from de jure segregation in that it:",
     ["Is mandated by law","Exists in practice through housing patterns and social customs, not by law","Is unconstitutional","Only applies to schools"],1,
     "De jure segregation is by law; de facto segregation results from social and economic factors."),

    ("Unit 3","Civil Liberties and Civil Rights","Hate Speech",
     "In the United States, hate speech is generally:",
     ["A criminal offense","Protected by the First Amendment unless it constitutes a direct threat or incitement","Always prohibited","Regulated by the FCC"],1,
     "Unlike many other democracies, the U.S. broadly protects offensive speech under the First Amendment."),

    ("Unit 3","Civil Liberties and Civil Rights","Student Speech Limits",
     "In Morse v. Frederick ('Bong Hits 4 Jesus'), the Court ruled that schools can restrict student speech that:",
     ["Is political","Promotes illegal drug use","Criticizes the school","Is religious"],1,
     "The Court held that schools have an interest in deterring drug use among students."),

    ("Unit 3","Civil Liberties and Civil Rights","Second Amendment Scope",
     "In District of Columbia v. Heller, the Court ruled that the Second Amendment:",
     ["Only protects militia members","Protects an individual's right to possess firearms for self-defense in the home","Allows unlimited gun ownership","Has been repealed"],1,
     "Heller was the first case to definitively establish an individual right to bear arms."),

    ("Unit 3","Civil Liberties and Civil Rights","Eminent Domain",
     "The 5th Amendment's Takings Clause requires that the government:",
     ["Can take property without limit","Provide just compensation when taking private property for public use","Never take private property","Only take property during war"],1,
     "Kelo v. City of New London expanded the definition of 'public use' to include economic development."),

    ("Unit 3","Civil Liberties and Civil Rights","Right to a Speedy Trial",
     "The 6th Amendment guarantees the right to a speedy trial, which means:",
     ["Trials must happen within 24 hours","The government cannot hold a defendant indefinitely before trial","All trials last one day","Defendants cannot request delays"],1,
     "This right protects against lengthy pretrial detention and the anxiety of unresolved charges."),

    ("Unit 3","Civil Liberties and Civil Rights","Grand Jury",
     "The 5th Amendment requires a grand jury for:",
     ["All criminal cases","Serious federal criminal charges, to determine if there is enough evidence to indict","Civil lawsuits","Traffic violations"],1,
     "Grand juries review evidence and decide whether to issue an indictment; they have not been fully incorporated to states."),

    ("Unit 3","Civil Liberties and Civil Rights","Civil Liberties vs Civil Rights",
     "Civil liberties differ from civil rights in that civil liberties:",
     ["Are granted by Congress","Protect individuals from government action, while civil rights protect against discrimination","Only apply to citizens","Are not in the Constitution"],1,
     "Civil liberties are freedoms FROM government interference; civil rights ensure equal TREATMENT by government."),

    ("Unit 3","Civil Liberties and Civil Rights","Plea Bargaining",
     "Plea bargaining is significant in the criminal justice system because:",
     ["It eliminates all trials","The vast majority of criminal cases are resolved through negotiated guilty pleas","It only applies to misdemeanors","Judges are not involved"],1,
     "Over 90% of federal criminal cases are resolved through plea bargains rather than trials."),

    ("Unit 3","Civil Liberties and Civil Rights","Substantive Due Process",
     "Substantive due process protects:",
     ["Only procedural fairness","Fundamental rights from government interference, even when proper procedures are followed","Economic rights only","The right to a jury trial"],1,
     "Substantive due process looks at whether the government has adequate justification for its actions."),

    # UNIT 4 additions (42 more → total 100)
    ("Unit 4","American Political Ideologies and Beliefs","Political Efficacy",
     "Political efficacy refers to:",
     ["Government efficiency","A citizen's belief that their participation in politics matters and can influence government","Voter apathy","Political corruption"],1,
     "High political efficacy increases voter turnout and civic engagement."),

    ("Unit 4","American Political Ideologies and Beliefs","Exit Polls",
     "Exit polls are conducted:",
     ["Before an election","As voters leave polling places to predict election outcomes","Only by the government","During debates"],1,
     "Media organizations use exit polls to project winners and understand voter motivations."),

    ("Unit 4","American Political Ideologies and Beliefs","Push Polls",
     "A push poll is designed to:",
     ["Gather accurate data","Influence respondents by asking leading or biased questions disguised as a survey","Test polling equipment","Predict future elections"],1,
     "Push polls are a campaign tactic that spreads negative information under the guise of polling."),

    ("Unit 4","American Political Ideologies and Beliefs","Benchmark Polls",
     "Benchmark polls are taken:",
     ["After an election","Early in a campaign to assess a candidate's initial standing","Only on Election Day","By interest groups"],1,
     "Campaigns use benchmark polls to establish a baseline of support and plan strategy."),

    ("Unit 4","American Political Ideologies and Beliefs","Tracking Polls",
     "Tracking polls are conducted:",
     ["Once per election","Continuously throughout a campaign to monitor shifts in opinion","Only in swing states","By the government"],1,
     "Daily or frequent polling helps campaigns detect changes in voter sentiment."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Age",
     "Research shows that as people age, they tend to:",
     ["Become more liberal","Become somewhat more conservative on economic and social issues","Stop voting","Change parties every decade"],1,
     "While not universal, studies suggest older voters lean more conservative than younger ones."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Education",
     "Higher levels of education are generally associated with:",
     ["Less political participation","More liberal views on social issues and higher levels of political engagement","Conservative economic views only","No change in political views"],1,
     "Education correlates with greater tolerance and engagement, though economic views vary."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Religion",
     "Religious attendance is most strongly correlated with:",
     ["Liberal social views","Conservative positions, particularly on social issues","No political views","Libertarian ideology"],1,
     "Regular churchgoers tend to hold more conservative views on issues like abortion and same-sex marriage."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Income",
     "Higher income levels tend to correlate with:",
     ["More liberal economic views","More conservative views on taxation and economic regulation","No political preferences","Socialist ideology"],1,
     "Wealthier individuals often favor lower taxes and less government economic intervention."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Race",
     "African Americans have historically aligned with:",
     ["The Republican Party","The Democratic Party since the New Deal and civil rights era","Third parties","No political party"],1,
     "Since the 1960s, African Americans have overwhelmingly supported Democratic candidates."),

    ("Unit 4","American Political Ideologies and Beliefs","Latino Political Views",
     "Latino voters in the United States generally:",
     ["Vote as a monolithic bloc","Have diverse political views varying by national origin, but lean Democratic overall","Always vote Republican","Do not participate in elections"],1,
     "Cuban Americans historically lean Republican while Mexican Americans lean Democratic."),

    ("Unit 4","American Political Ideologies and Beliefs","Priming",
     "Media priming refers to:",
     ["Printing newspapers","The media's ability to influence the criteria by which people evaluate political figures","Campaign advertising only","Social media algorithms"],1,
     "By emphasizing certain issues, the media shapes which factors voters use to judge leaders."),

    ("Unit 4","American Political Ideologies and Beliefs","Horse Race Journalism",
     "Horse race journalism focuses on:",
     ["Policy analysis","Campaign strategy, polls, and who is winning rather than substance","Investigative reporting","International news"],1,
     "Critics argue this approach prioritizes entertainment over informing voters about policy."),

    ("Unit 4","American Political Ideologies and Beliefs","Selective Exposure",
     "Selective exposure means that people tend to:",
     ["Watch all news sources equally","Seek out media that confirms their existing political beliefs","Avoid all news","Only read print newspapers"],1,
     "This contributes to political polarization as people consume one-sided information."),

    ("Unit 4","American Political Ideologies and Beliefs","Echo Chambers",
     "Political echo chambers are problematic because they:",
     ["Expose people to diverse viewpoints","Reinforce existing beliefs and contribute to political polarization","Increase voter turnout","Improve media literacy"],1,
     "When people only hear views they agree with, they become more extreme and less tolerant of opposition."),

    ("Unit 4","American Political Ideologies and Beliefs","Fiscal Conservative",
     "A fiscal conservative generally supports:",
     ["Higher taxes and more spending","Lower taxes, reduced government spending, and balanced budgets","Nationalized industries","Unlimited government borrowing"],1,
     "Fiscal conservatives prioritize reducing the national debt and limiting government economic intervention."),

    ("Unit 4","American Political Ideologies and Beliefs","Social Conservative",
     "A social conservative typically supports:",
     ["Progressive social policies","Traditional values, including opposition to abortion and support for religious liberty","Complete separation of church and state","Legalizing all drugs"],1,
     "Social conservatives emphasize traditional family structures and moral values in public policy."),

    ("Unit 4","American Political Ideologies and Beliefs","Progressive Ideology",
     "Progressives generally advocate for:",
     ["Maintaining the status quo","Government action to address inequality, expand rights, and reform institutions","Eliminating all government programs","Returning to earlier policies"],1,
     "Modern progressives push for systemic changes to address social and economic disparities."),

    ("Unit 4","American Political Ideologies and Beliefs","Neoconservatism",
     "Neoconservatives are distinguished by their support for:",
     ["Isolationism","An assertive foreign policy and the promotion of democracy abroad","Reduced military spending","Pacifism"],1,
     "Neoconservatives advocate using American power, including military force, to spread democratic values."),

    ("Unit 4","American Political Ideologies and Beliefs","Socialism in America",
     "Democratic socialism in the United States advocates for:",
     ["Government ownership of all property","Expanded social programs within a democratic framework, such as universal healthcare","Abolishing elections","Complete free-market capitalism"],1,
     "American democratic socialists seek Nordic-style social programs while maintaining democratic governance."),

    ("Unit 4","American Political Ideologies and Beliefs","Public Opinion on Healthcare",
     "Public opinion polling consistently shows that Americans:",
     ["Unanimously support single-payer healthcare","Are divided on healthcare policy, with support varying by how the question is framed","Never think about healthcare","All oppose government involvement"],1,
     "Framing effects significantly influence poll results on healthcare policy."),

    ("Unit 4","American Political Ideologies and Beliefs","Party Identification",
     "Party identification is most strongly influenced by:",
     ["Campaign advertising","Family and early socialization experiences","A single election","Media consumption alone"],1,
     "Most people adopt the party affiliation of their parents, making it resistant to change."),

    ("Unit 4","American Political Ideologies and Beliefs","Dealignment",
     "Dealignment occurs when:",
     ["Parties become stronger","Voters move away from party identification and become more independent","A new party replaces an old one","Voters switch parties permanently"],1,
     "Dealignment reflects growing distrust of both major parties and an increase in independent voters."),

    ("Unit 4","American Political Ideologies and Beliefs","Partisan Polarization",
     "Partisan polarization has increased in recent decades, meaning that:",
     ["Parties have become more moderate","The ideological distance between Democrats and Republicans has grown significantly","Third parties have gained power","Voter turnout has decreased"],1,
     "Research shows increasing ideological homogeneity within parties and growing gaps between them."),

    ("Unit 4","American Political Ideologies and Beliefs","Trust in Government",
     "Trust in the federal government has generally:",
     ["Increased steadily since 1960","Declined significantly since the 1960s, with occasional temporary increases","Remained constant","Never been measured"],1,
     "Events like Vietnam, Watergate, and partisan conflict have eroded public trust over decades."),

    ("Unit 4","American Political Ideologies and Beliefs","Political Knowledge",
     "Research shows that most Americans:",
     ["Are well-informed about politics","Have relatively low levels of political knowledge, especially about specific policies","Follow politics closely","Can name all Supreme Court justices"],1,
     "Political knowledge varies widely and tends to be higher among older, wealthier, and more educated citizens."),

    ("Unit 4","American Political Ideologies and Beliefs","Policy Mood",
     "The concept of 'policy mood' refers to:",
     ["Individual policy preferences","The general ideological direction of public opinion at a given time","Congressional voting patterns","Presidential approval ratings"],1,
     "Policy mood shifts between liberal and conservative periods, influencing which policies are politically viable."),

    ("Unit 4","American Political Ideologies and Beliefs","Crosscutting Cleavages",
     "Crosscutting cleavages in public opinion occur when:",
     ["Everyone agrees on every issue","An individual's group memberships pull them in different political directions","There is no political conflict","Only one issue matters"],1,
     "A wealthy African American, for example, may face conflicting pressures on economic vs. social issues."),

    ("Unit 4","American Political Ideologies and Beliefs","Wedge Issues",
     "A wedge issue is designed to:",
     ["Unite voters","Split the opposing party's coalition by highlighting a divisive topic","Reduce voter turnout","Promote bipartisanship"],1,
     "Campaigns use wedge issues to peel off voters from the opposition by exploiting internal divisions."),

    ("Unit 4","American Political Ideologies and Beliefs","Rally Around the Flag",
     "The 'rally around the flag' effect occurs when:",
     ["Voter turnout drops","Presidential approval ratings spike temporarily during international crises","Congress passes a popular law","The economy improves"],1,
     "National security events tend to produce short-term increases in presidential approval."),

    ("Unit 4","American Political Ideologies and Beliefs","Approval Ratings",
     "Presidential approval ratings are most influenced by:",
     ["The president's personality","Economic conditions and major events","The first lady's popularity","Weather patterns"],1,
     "The economy is the strongest predictor of presidential approval over time."),

    ("Unit 4","American Political Ideologies and Beliefs","Ideology and Gender",
     "The gender gap in American politics shows that women are more likely than men to:",
     ["Vote Republican","Support Democratic candidates and favor government social programs","Not vote","Support military intervention"],1,
     "Women tend to prioritize healthcare, education, and social welfare, aligning them with Democratic positions."),

    ("Unit 4","American Political Ideologies and Beliefs","Rural vs Urban Divide",
     "The urban-rural divide in American politics shows that:",
     ["Rural areas vote Democratic","Urban areas tend to vote Democratic while rural areas tend to vote Republican","There is no geographic voting pattern","Suburban areas don't vote"],1,
     "This geographic sorting has become one of the most significant cleavages in American politics."),

    ("Unit 4","American Political Ideologies and Beliefs","Social Media and Politics",
     "Social media has changed American politics by:",
     ["Reducing political engagement","Enabling rapid mobilization, direct communication, and the spread of misinformation","Having no effect on elections","Replacing all traditional media"],1,
     "Social media amplifies voices and speeds information sharing but also facilitates polarization."),

    ("Unit 4","American Political Ideologies and Beliefs","Civic Duty",
     "The concept of civic duty suggests that citizens:",
     ["Have no obligation to participate","Have a responsibility to vote and participate in democratic processes","Should only vote if they are informed","Must join a political party"],1,
     "Civic duty is a significant motivator for voter turnout, especially in presidential elections."),

    ("Unit 4","American Political Ideologies and Beliefs","Incumbency Advantage",
     "Incumbents have an advantage in elections because of:",
     ["Term limits","Name recognition, access to campaign funds, and the ability to provide constituent services","Being the challenger","Running in open seats"],1,
     "Congressional incumbents win reelection over 90% of the time due to these structural advantages."),

    ("Unit 4","American Political Ideologies and Beliefs","Mandate Theory",
     "The mandate theory of elections holds that:",
     ["Elections are meaningless","A winning candidate has a mandate from the people to implement their proposed policies","Only landslide victories matter","Mandates only apply to presidents"],1,
     "Presidents often claim a mandate after winning, though the theory is debated by political scientists."),

    ("Unit 4","American Political Ideologies and Beliefs","Culture War",
     "The 'culture war' in American politics refers to:",
     ["Military conflict","Deep divisions over social issues like abortion, LGBTQ+ rights, and religion in public life","Economic policy debates","Foreign policy disagreements"],1,
     "These social and cultural disagreements have become central to partisan identity."),

    ("Unit 4","American Political Ideologies and Beliefs","Libertarian vs Populist",
     "The key difference between libertarians and populists is that:",
     ["They agree on everything","Libertarians want less government in both economic and social areas while populists want more in both","Populists are always liberal","Libertarians support high taxes"],1,
     "This distinction maps to the two-dimensional political spectrum beyond simple left-right."),

    ("Unit 4","American Political Ideologies and Beliefs","Media Bias",
     "Studies on media bias generally find that:",
     ["All media is equally biased","Bias varies by outlet, and consumers increasingly choose partisan sources that match their views","There is no bias in any media","Only TV news is biased"],1,
     "The proliferation of media choices allows consumers to self-select into ideological bubbles."),

    ("Unit 4","American Political Ideologies and Beliefs","Federalism and Ideology",
     "Conservative support for states' rights reflects the belief that:",
     ["The federal government should control everything","State governments are closer to the people and better positioned to address local needs","States should have no power","Only the Supreme Court should decide policy"],1,
     "Conservatives often invoke federalism to argue against federal regulation and mandates."),

    # UNIT 5 additions (34 more → total 100)
    ("Unit 5","Political Participation","Caucuses",
     "A caucus differs from a primary election because it:",
     ["Is a secret ballot","Involves public discussion and voting at local meetings rather than a traditional ballot","Is run by the federal government","Only nominates vice presidents"],1,
     "Caucuses require greater time commitment and tend to attract more ideologically motivated participants."),

    ("Unit 5","Political Participation","Frontloading",
     "Frontloading in the presidential nomination process refers to:",
     ["Delaying primaries","States moving their primaries earlier in the calendar to gain more influence","Loading ballots with extra candidates","Adding more debate questions"],1,
     "States compete to hold early contests because early results shape momentum and media coverage."),

    ("Unit 5","Political Participation","Superdelegates",
     "Superdelegates in the Democratic Party are:",
     ["Elected by voters in primaries","Party leaders and elected officials who can vote for any candidate at the convention","Required to follow primary results","Also used by Republicans"],1,
     "Superdelegates give party elites some influence over the nomination process."),

    ("Unit 5","Political Participation","Convention Bounce",
     "A 'convention bounce' refers to:",
     ["Physical activity at conventions","A temporary increase in a candidate's poll numbers after their party's national convention","A permanent shift in support","Decreased media coverage"],1,
     "Conventions generate positive media coverage that typically produces a short-term polling boost."),

    ("Unit 5","Political Participation","Swing States",
     "Swing states receive disproportionate attention from campaigns because:",
     ["They have the most electoral votes","Their outcomes are uncertain and could go to either party","They always vote for the winner","They hold the earliest primaries"],1,
     "Candidates focus resources on competitive states where their effort can change the outcome."),

    ("Unit 5","Political Participation","Soft Money",
     "Soft money in campaign finance refers to:",
     ["Direct donations to candidates","Funds raised by parties for 'party-building activities' that were largely unregulated before BCRA","Government campaign funding","Small individual donations"],1,
     "The Bipartisan Campaign Reform Act of 2002 banned national party soft money."),

    ("Unit 5","Political Participation","527 Organizations",
     "527 organizations are:",
     ["Part of the federal government","Tax-exempt groups that engage in political activities without directly advocating for candidates","Regulated by the FEC","The same as Super PACs"],1,
     "527s can raise unlimited money for issue advocacy and voter mobilization."),

    ("Unit 5","Political Participation","Dark Money",
     "Dark money in politics refers to:",
     ["Illegal campaign contributions","Political spending by nonprofit organizations that do not disclose their donors","Government slush funds","Foreign campaign donations"],1,
     "501(c)(4) organizations can engage in politics without revealing who funds them."),

    ("Unit 5","Political Participation","BCRA",
     "The Bipartisan Campaign Reform Act (McCain-Feingold) primarily:",
     ["Eliminated all campaign finance rules","Banned soft money donations to national parties and restricted issue ads before elections","Created the Electoral College","Established term limits"],1,
     "BCRA addressed loopholes in campaign finance law, though Citizens United later weakened some provisions."),

    ("Unit 5","Political Participation","Prospective Voting",
     "Prospective voting occurs when voters:",
     ["Look backward at past performance","Make choices based on what they expect a candidate will do in the future","Vote randomly","Always support incumbents"],1,
     "Prospective voters evaluate candidates' policy proposals and promises."),

    ("Unit 5","Political Participation","Party-Line Voting",
     "Party-line voting has increased in recent years, which means:",
     ["Voters split tickets more often","More voters choose candidates of the same party for all offices on the ballot","Third parties are winning","Turnout is declining"],1,
     "Increased polarization has reduced split-ticket voting across most elections."),

    ("Unit 5","Political Participation","Ballot Initiatives",
     "A ballot initiative allows:",
     ["Only legislators to propose laws","Citizens to propose and vote directly on legislation or constitutional amendments","The president to bypass Congress","Judges to create new laws"],1,
     "Direct democracy mechanisms like initiatives give citizens a way to enact policy without legislators."),

    ("Unit 5","Political Participation","Recall Elections",
     "A recall election allows voters to:",
     ["Elect new candidates only","Remove an elected official from office before their term ends","Choose Supreme Court justices","Override a presidential veto"],1,
     "Recalls are available in some states and provide a check on elected officials between regular elections."),

    ("Unit 5","Political Participation","Voter ID Laws",
     "Supporters of voter ID laws argue they:",
     ["Suppress minority votes","Prevent voter fraud and protect election integrity","Increase turnout","Are unconstitutional"],1,
     "The debate centers on election security versus concerns about disenfranchising eligible voters."),

    ("Unit 5","Political Participation","Early Voting",
     "Early voting and mail-in ballots have:",
     ["Decreased voter access","Expanded access to voting and increased convenience for many citizens","Had no effect on turnout","Been banned in most states"],1,
     "These methods reduce barriers to voting, particularly for working people and those with limited mobility."),

    ("Unit 5","Political Participation","Motor Voter Act",
     "The National Voter Registration Act (Motor Voter) requires:",
     ["All citizens to vote","States to offer voter registration when citizens apply for driver's licenses","Mandatory voting","Automatic citizenship for voters"],1,
     "The law simplified registration by integrating it with common government interactions."),

    ("Unit 5","Political Participation","Socioeconomic Status and Voting",
     "Voter turnout tends to increase with:",
     ["Lower income","Higher income, education, and age","Younger age","Rural residence"],1,
     "Socioeconomic factors are among the strongest predictors of political participation."),

    ("Unit 5","Political Participation","Rational Ignorance",
     "Rational ignorance occurs when citizens:",
     ["Are uninformed due to laziness","Decide that the cost of becoming informed outweighs the expected benefit","Are prohibited from learning","Only watch one news source"],1,
     "Since one vote rarely decides an election, some citizens rationally choose not to invest in political knowledge."),

    ("Unit 5","Political Participation","Free Rider Problem",
     "The free rider problem in interest group politics occurs when:",
     ["Everyone pays dues","People benefit from a group's efforts without contributing to it","Groups have too many members","All members participate equally"],1,
     "This challenge makes it harder for large groups to organize effectively."),

    ("Unit 5","Political Participation","Selective Benefits",
     "Interest groups overcome the free rider problem by offering:",
     ["Nothing to members","Selective benefits available only to members, such as discounts or publications","Government contracts","Tax exemptions to non-members"],1,
     "Material, solidary, and purposive incentives encourage individuals to join and contribute."),

    ("Unit 5","Political Participation","Grassroots Lobbying",
     "Grassroots lobbying involves:",
     ["Hiring professional lobbyists","Mobilizing ordinary citizens to contact their representatives about an issue","Filing lawsuits","Running campaign ads"],1,
     "Interest groups use grassroots campaigns to demonstrate broad public support for their positions."),

    ("Unit 5","Political Participation","Revolving Door",
     "The 'revolving door' in politics refers to:",
     ["Turnstiles at government buildings","The movement of personnel between government positions and private sector lobbying jobs","Term limits","Frequent elections"],1,
     "Critics argue this creates conflicts of interest and gives special interests undue influence."),

    ("Unit 5","Political Participation","Electioneering",
     "Electioneering by interest groups includes:",
     ["Only donating money","Endorsing candidates, running ads, mobilizing voters, and contributing to campaigns","Filing amicus briefs only","Writing legislation"],1,
     "Interest groups use multiple strategies to influence election outcomes."),

    ("Unit 5","Political Participation","Plurality vs Majority",
     "In a plurality election system, the winner:",
     ["Must get over 50% of the vote","Needs only the most votes, not necessarily a majority","Must win every state","Is chosen by the Electoral College"],1,
     "Most U.S. elections use plurality (first-past-the-post), which disadvantages third parties."),

    ("Unit 5","Political Participation","Proportional Representation",
     "Proportional representation systems tend to produce:",
     ["Two-party systems","Multi-party systems where seats are allocated based on vote share","One-party rule","No political parties"],1,
     "PR systems give smaller parties representation, unlike winner-take-all systems."),

    ("Unit 5","Political Participation","National Party Committees",
     "The national party committees (DNC and RNC) primarily:",
     ["Write legislation","Coordinate campaign strategy, fundraising, and party messaging","Confirm judicial nominees","Govern states"],1,
     "National committees play a crucial role in supporting candidates and building party infrastructure."),

    ("Unit 5","Political Participation","Presidential Coattails",
     "The 'coattail effect' refers to:",
     ["Fashion at political events","The ability of a popular presidential candidate to help other party candidates win","Always winning the popular vote","Third-party success"],1,
     "Strong presidential candidates can boost turnout and support for down-ballot party members."),

    ("Unit 5","Political Participation","Divided Government",
     "Divided government occurs when:",
     ["One party controls everything","Different parties control the presidency and at least one chamber of Congress","The Supreme Court disagrees with Congress","States oppose federal policy"],1,
     "Divided government can lead to gridlock but also forces compromise between parties."),

    ("Unit 5","Political Participation","Malapportionment",
     "Malapportionment refers to:",
     ["Equal district populations","Unequal representation caused by districts with significantly different population sizes","Gerrymandering","Voter suppression"],1,
     "Baker v. Carr and Reynolds v. Sims addressed malapportionment by requiring equal population districts."),

    ("Unit 5","Political Participation","Packing and Cracking",
     "In gerrymandering, 'packing' and 'cracking' refer to:",
     ["Moving people between districts","Concentrating opposition voters in few districts (packing) or spreading them thin (cracking)","Increasing voter turnout","Eliminating districts"],1,
     "These techniques allow map-drawers to dilute the electoral power of opposing party voters."),

    ("Unit 5","Political Participation","Midterm Election Patterns",
     "The president's party typically loses seats in midterm elections because:",
     ["The president campaigns too much","Lower turnout benefits the opposition and voters often express dissatisfaction with the ruling party","Midterms always favor Republicans","The Constitution requires it"],1,
     "This pattern has held in most midterm elections throughout American history."),

    ("Unit 5","Political Participation","Faithless Electors",
     "A faithless elector is one who:",
     ["Always follows state results","Votes for a candidate other than the one they pledged to support","Is removed from the Electoral College","Abstains from voting"],1,
     "While rare, some states have laws penalizing faithless electors, upheld in Chiafalo v. Washington (2020)."),

    ("Unit 5","Political Participation","Battleground State Strategy",
     "Campaigns focus on battleground states because:",
     ["They are the largest states","These competitive states determine the Electoral College outcome, making campaign resources most effective there","They have the earliest primaries","All voters there are undecided"],1,
     "The winner-take-all system means campaigns ignore safe states and target those that could go either way."),

    ("Unit 5","Political Participation","Political Action Committees",
     "Traditional PACs are limited in that they:",
     ["Can raise unlimited funds","Have contribution limits and must disclose donors, but can donate directly to candidates","Cannot spend any money","Only support third parties"],1,
     "PACs face stricter regulations than Super PACs but have the advantage of direct candidate contributions."),

    ("Unit 3","Civil Liberties and Civil Rights","Right to Privacy",
     "In Griswold v. Connecticut (1965), the Supreme Court ruled that the Constitution contains:",
     ["An explicit right to privacy in the First Amendment","A right to privacy found in the penumbras of the Bill of Rights","No protection for marital privacy","A right to privacy only for government officials"],1,
     "The Court found a right to privacy in the penumbras (implied zones) of several Bill of Rights amendments."),

    ("Unit 4","American Political Ideologies and Beliefs","Political Socialization",
     "Which factor is generally considered the strongest agent of political socialization?",
     ["The media","Peer groups","Family","Religious institutions"],2,
     "Family is widely regarded as the most influential agent of political socialization, shaping early political attitudes."),
]


def build_questions():
    """Convert raw tuples into question dicts with balanced answer distribution."""
    # Verify we have questions
    assert len(RAW) == 500, f"Expected 500 questions, got {len(RAW)}"

    # We'll shuffle correct answers across A/B/C/D positions
    # Target: ~125 of each letter
    import random
    random.seed(42)  # Reproducible

    # Assign target letters round-robin then shuffle
    target_letters = []
    for i in range(len(RAW)):
        target_letters.append(i % 4)  # 0=A,1=B,2=C,3=D
    random.shuffle(target_letters)

    questions = []
    letter_map = {0: "A", 1: "B", 2: "C", 3: "D"}

    for idx, (raw, target_pos) in enumerate(zip(RAW, target_letters)):
        unit, unit_name, concept, question, options, correct_idx, explanation = raw

        # We need to move the correct answer to target_pos
        # Create new options list with correct answer at target_pos
        correct_option = options[correct_idx]
        wrong_options = [opt for i, opt in enumerate(options) if i != correct_idx]

        # Build new options array
        new_options = []
        wrong_idx = 0
        for pos in range(4):
            if pos == target_pos:
                new_options.append(correct_option)
            else:
                new_options.append(wrong_options[wrong_idx])
                wrong_idx += 1

        questions.append({
            "id": idx + 1,
            "unit": unit,
            "unitName": unit_name,
            "concept": concept,
            "question": question,
            "options": new_options,
            "answer": letter_map[target_pos],
            "explanation": explanation,
        })

    # Verify distribution
    from collections import Counter
    dist = Counter(q["answer"] for q in questions)
    print(f"Answer distribution: {dict(sorted(dist.items()))}")

    # Verify unit distribution
    unit_dist = Counter(q["unit"] for q in questions)
    print(f"Unit distribution: {dict(sorted(unit_dist.items()))}")

    return questions


def write_question_bank(questions):
    """Write question_bank.py file."""
    lines = []
    lines.append('"""')
    lines.append("AP U.S. Government & Politics — 500-Question Bank")
    lines.append("Balanced answer distribution across A/B/C/D.")
    lines.append("Covers all 5 AP Gov units with stimulus-based questions.")
    lines.append('"""')
    lines.append("")
    lines.append("QUESTION_BANK = [")

    unit_labels = {
        "Unit 1": "Foundations of American Democracy",
        "Unit 2": "Interactions Among Branches of Government",
        "Unit 3": "Civil Liberties and Civil Rights",
        "Unit 4": "American Political Ideologies and Beliefs",
        "Unit 5": "Political Participation",
    }
    current_unit = None

    for q in questions:
        # Add unit header comment (based on first occurrence in sorted order)
        # Actually, questions are shuffled so just output them
        entry = json.dumps(q, ensure_ascii=False)
        lines.append(f"    {entry},")

    lines.append("]")
    lines.append("")

    with open("/Users/yulinglin/Documents/AP gov/question_bank.py", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Wrote {len(questions)} questions to question_bank.py")


if __name__ == "__main__":
    questions = build_questions()
    write_question_bank(questions)
