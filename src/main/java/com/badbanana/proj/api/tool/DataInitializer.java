
package com.badbanana.proj.api.tool;

import com.badbanana.proj.api.model.LawCase;
import com.badbanana.proj.api.model.Relevance;
import com.badbanana.proj.api.repository.CaseRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

/**
 * initial data at application startup.
 */
@Component
public class DataInitializer implements CommandLineRunner {

    @Autowired
    CaseRepository caseRepository;

    @Override
    public void run(String... arg0) throws Exception {
//        addCase1();
    }

    private void addCase1() {
        LawCase c = new LawCase();
        c.setCaseName("In the matter of RCG CBD Pty Ltd");
        c.setMnc("[2016] NSWSC 1938");
        c.setDecision("Ninth defendant substituted. Liquidator personally pay costs.");
        c.setJurisdiction("Equity - Corporations List");
        c.setDecisionDate("24 October 2016");
        c.setDecision("Ninth defendant substituted. Liquidator personally pay costs");
        c.setCatchwords("CORPORATIONS – winding up – application for substitution of a defendant – present defendant as a result of inquiries made and traces obtained through ATO – whether (NSW) Civil Procedure Act 2005, s 65, applies – clear that liquidator’s intention was to sue person who received payment by company – only reason party was sued was mistaken belief that person in receipt of payment was present defendant – whether substitution should be declined as a matter of discretion – no connection between present ninth defendant and substituted party – present ninth defendant repeatedly brought to liquidator’s attention its mistake – expiry of 3-year limitation period – no evidence of prejudice – application can be brought outside of 3-year period if shelf order obtained");
        c.setCategory("Procedural and other rulings");
        c.setParties("Mitchell Warren Ball (first plaintiff); RCG CBD Pty Ltd (second plaintiff); Banq Accountants and Advisors Pty Ltd (first defendant); Wenman Brimak Investments Pty Ltd (second defendant); Statewide Printing Group Pty Ltd (third defendant); Sivasli Pty Ltd (fifth defendant); Harry Patsouris (sixth defendant); Kitto Investments Pty Ltd (seventh defendant); Fox & Staniland Pty Ltd (eighth defendant); Kazzi Investments Pty Ltd (ninth defendant); JRC Kazzi Investments Pty Limited ACN 141 174 745 (proposed ninth defendant); Coolfind Pty Ltd (tenth defendant)");
        c.setJudgment("1\tHIS HONOUR: On 13 October 2016, I dismissed an application by the first plaintiff Mitchell Warren Ball as liquidator of the second plaintiff RCG CBD Pty Limited, whereby the liquidator sought to have Nadia Bevilaqua substituted as eighth defendant in place of Fox & Staniland pursuant to (NSW) Civil Procedure Act 2005, s 64 and s 65. In that case, I did so because, as explained at [19] of the judgment ([2016] NSWSC 1937), the only intention that could be gleaned from the statement of claim, and the limited evidence that was adduced, was that the liquidator intended to sue the firm of solicitors to whom the payment was made – which was correctly identified as the then eighth defendant and not that firm's client – in circumstances where the liquidator knew that the payment was to the solicitor's trust account, had sought details about who the client was, and then in any event sued the solicitor. In those circumstances, there was nothing to indicate that the solicitor really intended to sue the beneficiary as distinct from the recipient of the payment.\n" +
                "2\tBefore the Court today is another application by Mr Ball as liquidator of the same company; this time to substitute as the ninth defendant JRC Kazzi Investments Pty Limited ACN 141 174 745 in place of the current ninth defendant Kazzi Investments Pty Limited ACN 140 032 122. The statement of claim as originally pleaded against the ninth defendant is as follows: CLAIM AGAINST NINTH DEFENDANT: The Kazzi Payment: 86. On 30 August 2012 (\"relevant period\") the company made a payment to the ninth defendant in the total sum of $70,000 referred to herein as the Kazzi payment as particularised in the table below. The particulars set out the date of the payment as 30 August 2012, the amount as $70,000 and the account number to which it was paid. 87. The Kazzi payment to the ninth defendant was a transaction of the company within the meaning of section 9 and 588FE of the Act.\n" +
                "3\tThe pleading then proceeds to allege that the payment was an insolvent transaction, an uncommercial transaction, an unreasonable director-related transaction and a voidable transaction. Subsequent allegations are that the Kazzi payment was moneys had and received by the ninth defendant for the use of the company, and that the ninth defendant was obliged to repay the amount of the Kazzi payment and, alternatively, that it was a loan due by the ninth defendant to the company.\n" +
                "4\tThe evidence establishes that the liquidator sued the present ninth defendant because, on inquiries made and traces obtained through the Australian Taxation Office, it appeared to be the party which had received the payment. The evidence of that was less than perfect, but it sufficed for the liquidator to decide that that was the name of the party that he wanted to sue. The original ninth defendant, objected before proceedings were commenced, that it had never received moneys from the company and it renewed those objections after it was sued. The liquidator pressed on, in the absence of any evidence to make good the protestations of the ninth defendant. However, subsequent inquiries revealed that an unrelated but similarly named company – the proposed substituted defendant – was in fact the recipient of the payment.\n" +
                "5\tIn Bridge Shipping Pty Limited v Grand Shipping SA (1991) 173 CLR 231 McHugh J, with whom Brennan, Deane and Toohey JJ agreed, said (at 260): Moreover, a plaintiff may make 'a mistake in the name of a party' not only because the plaintiff mistakenly believes that a certain person whom the plaintiff can otherwise identify bears a certain name, but also because the plaintiff mistakenly believes that a person who answers a particular description bears a certain name. Thus a plaintiff may make a mistake 'in the name of a party' because although intending to sue a particular person whom the plaintiff knows by sight, the plaintiff is mistaken as to that person's name. Equally, the plaintiff may make a mistake 'in the name of a party' because although intending to sue a person whom the plaintiff knows by a particular description, for example, the driver of a certain car, the plaintiff is mistaken as to the name of the person who answers that description. In both cases the plaintiff knows the person intending to be sued by reference to some property or properties which is or are peculiar to that person, but is mistaken as to the name of that person. In the first case the properties which identify the person are personal characteristics; in the second case they are the properties which are of the essence of the description of that person. But for the purposes of the rule in question, subrule 4 in that case, that distinction is irrelevant. In both cases the plaintiff was mistaken only as to the name of the person intended to be sued.\n" +
                "6\tHis Honour went on to express the view (at 261): If Bridge had intended to sue the carrier and had mistakenly believed that the name of the carrier was Grand, it would follow that Bridge had made a mistake in the name of the party.\n" +
                "7\tHis Honour went on to elaborate on that proposition. The application in Bridge v Grand ultimately failed because the Court concluded that Bridge had not intended to sue the carrier mistakenly believing that its name was Grand, but had intended to sue the owner. The mistake was therefore not in the name but in identifying who was liable.\n" +
                "8\tIn Environinvest Ltd v Former Partnership of Webster, White, Gridley, Nairn, Newman, Peters and Miller (2012) 208 FCR 376, Justice Gordon referred to Bridge Shipping and said (at [22]): One way of seeking to determine whether in Environinvest's application property falls within rule 8.21 of the Federal Court Reports is to ask two questions. First, did Environinvest intend to sue its auditor; secondly, if so, did it mistakenly believe that the identity of the auditor was the corporate entity. In substance, these were the questions posed in Bridge Shipping. In the present case the answers to those questions are straightforward \"Yes\" and \"yes\" respectively\n" +
                "9\tIn the present case, both the statement of claim and the affidavit evidence makes clear that the intention of the liquidator was always to sue the person who received the payment made by the company. The person sued was identified from the payments made in the bank statements, and the name which appeared against the payment recorded in the bank statement. Traces were then undertaken to seek to confirm its corporate identity. In fact, the wrong corporate identity was confirmed, but that does not change the fact that the liquidator intended to sue a person who met the description of the recipient of the impugned payment from the company. In that respect, this application is quite different from the application that I dealt with a fortnight ago. Thus Gordon J's first question, did the liquidator intend to sue the recipient of the payment, is shortly answered yes.\n" +
                "10\tThe second question then is, did it mistakenly believe that the identity of the person who received the payment was Kazzi Investments, the ninth defendant originally sued? The answer again, obviously, is yes. The only reason that party was sued was that the liquidator believed that that was the name of the party who had received the payment in question from the company.\n" +
                "11\tAccordingly, the grounds for the application of Civil Procedure Act, s 65, are established.\n" +
                "12\tThe respondent to the application submits that substitution should nonetheless be declined as a matter of discretion. There are a number of factors that favour that proposition. First and foremost is that unlike many cases in which s 65 is invoked, this is not a case in which the wrong entity in a related company group has been sued, or in which the party sought to be substituted would necessarily have been on notice of the proceedings because of the minor nature of the mistake in question. There is no connection between the parties sought to be substituted and that originally sued, and no reason to suspect that it would have been on notice of the proceedings until the joinder application was made.\n" +
                "13\tThe second discretionary factor is that Kazzi Investments, the company that was incorrectly sued, repeatedly brought to the liquidator's attention the circumstance that it had had no dealings with the company and protested that it had no liability, and the liquidator pressed on regardless.\n" +
                "14\tAgainst that the respondent points to no prejudice arising from its substitution at this stage. It is true that the limitation period of three years has otherwise expired, unless advantage can be taken of s 65. In that way, there will be in effect a proceeding brought against the substituted defendant outside the three year period provided by (CTH) Corporations Act 2001, s 588GA. That said, that can often occur, particularly when a shelf order is obtained without notice to respondents in this type of case. If there were prejudice arising from the proceeding being brought after the three year period, other than the mere exposure to a claim which would otherwise be extinguished, that would have been a powerful answer to such an application. In particular, if the respondent had argued that it had in some way relied upon the expiration of the period, or no longer had available to it evidence that would have been available earlier, that may well have been a powerful argument on the exercise of discretion. But in the absence of any evidence of prejudice, coupled with the circumstance that applications of this kind can be brought outside the three year period if a shelf order has been obtained, it seems to me that on balance there is less injustice in granting the order sought than in refusing it.\n" +
                "15\tThe Court orders that: (1)\tPursuant to Civil Procedure Act, s 64 and s 65, JRC Kazzi Investments Pty Limited (ACN 141 174 745) be substituted as ninth defendant in place of Kazzi Investments Pty Limited (ACN 140 032 122).\n" +
                "16\tBy consent between the plaintiff, and the former ninth defendant, the Court further orders that: (1)\tThe liquidator personally pay the costs of Kazzi Investments Pty Ltd ACN 140 032 122, such costs to be payable forthwith, but not to incur interest if paid within 30 days of assessment or agreement.");

        c.setUrl("http://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/nsw/NSWSC/2016/1938.html");

        List<Relevance> relevances = new ArrayList<>();
        Relevance r1 = new Relevance();
        r1.setTitle("MARTIN BRUCE JONES As Liquidator of Forge Group Ltd (Receivers and Managers Appointed) (In Liquidation) -v- SUN ENGINEERING (QLD) PTY LTD [2017] WASC 195 (27 July 2017)");
        r1.setUrl("http://www.austlii.edu.au/cgi-bin/viewdoc/au/cases/wa/WASC/2017/195.html?context=1;query=In%20the%20matter%20of%20RCG%20CBD%20Pty%20Ltd");
        r1.setValue("65%");

        relevances.add(r1);
        c.setRelevance(relevances);

        this.caseRepository.save(c);

    }



}