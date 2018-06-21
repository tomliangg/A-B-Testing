# A-B-Testing-CMPT353_e6_p1
<h3>This repo is created for documentation purpose. The repo contains my personal work toward the SFU CMPT353 (Computational Data Science) course. You may use my solution as a reference. The .zip archive contains the original exercise files. For practice purpose, you can download the .zip archive and start working from there.</h3>

<p><a href="https://coursys.sfu.ca/2018su-cmpt-353-d1/pages/AcademicHonesty">Academic Honesty</a>: it's important, as always.</p>
<br/>
<p> The task of this exercise is to perform A/B test on a search tool. You need to find out whether the new or old search tool have more usages.</p>
<br/>
<p>Below is the exercise description </p>
<hr>

<h2 id="h-a-b-testing">A/B Testing</h2>
<p>A very common technique to evaluate changes in a user interface is <a href="https://en.wikipedia.org/wiki/A/B_testing">A/B testing</a>: show some users interface A, some interface B, and then look to see if one performs better than the other.</p>
<p>I started an A/B test on CourSys a few months ago. I wanted to use it for this question, and it was going to be awesome. Then I learned that there was no significance anywhere and the numbers were much too small. So I faked some data. That's life, I guess.</p>
<p>The provided <code>searches.json</code> (load with Pandas using <code>orient='records', lines=True</code>) has information about users' usage of the <span>&ldquo;</span>search<span>&rdquo;</span> feature, which is where the A/B test happened. Users <strong>with an odd-numbered uid were shown a new-and-improved search box</strong>. Others were shown the original design.</p>
<p>The question I was interested in: do people search more with the new design? I see a few ways to approach that problem:</p>
<ul><li>Did more users use the search feature? (More precisely: did a different fraction of users have search count <span>&gt;</span> 0?)
</li><li>Did users search more often? (More precisely: is the number of searches per user different?)
</li></ul>
<p>The number of searches is far from being normal. Unless you're more clever than me, you won't be able to transform it to anything that looks even slightly normal. (Data is integers, mostly zero. No transform will have much to work with.) As a result, we're going to be using <strong>nonparametric</strong> tests.</p>
<p>Create a program <code>ab_analysis.py</code> that takes an input file on the command line, and analyses the provided data to get p-values for the above questions. The provided <code>ab_analysis_hint.py</code> gives a template for output. </p>
<p><a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html">Hint 1</a>. <a href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html">Hint 2</a>. In your contingency table, your categories will be even/odd uid (aka control/treatment), and <span>&ldquo;</span>searched at least once<span>&rdquo;</span>/<span>&ldquo;</span>never searched<span>&rdquo;</span>.</p>
<p>When analysing the (real, not faked) data, I realized: I don't care so much about <strong>all</strong> users. Instructors are the ones who can get more useful information from the search feature, so perhaps non-instructors didn't touch the search feature because it was genuinely not relevant to them.</p>
<p>Maybe we should ask about what happened to just the instructors from our data set. <strong>Repeat the above analysis looking only at instructors</strong>.</p>
<p>Report all of the p-values in the output format specified in the hint. [And note the question at the bottom about your results.]</p>
