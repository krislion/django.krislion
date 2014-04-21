from django import http

SUBDOMAINS = [
    '12thMan'
    ,'BOOK'
    ,'BrownAle'
    ,'CANADA'
    ,'CONCEPT'
    ,'DAVERYACK'
    ,'DEVIANT'
    ,'DRONES'
    ,'FACEBOOK'
    ,'GITHUB'
    ,'KRISLION'
    ,'LINKEDIN'
    ,'MARA'
    ,'MULLINS'
    ,'MUSIC'
    ,'MYSPACE'
    ,'NICK'
    ,'PROFILE'
    ,'PURCHASE'
    ,'RANDY'
    ,'STEAM'
    ,'TAYLOR'
    ,'TOM'
    ,'TWITTER'
    ,'YUSUKE'
    ,'ZESTAWIT'
] #SUBDOMAINS


DEFAULT_PAGE='''
<html>
<head><title>Kris Lion</title>
<style type="text/css">
body {background-color:#ffffff;color:#ffffff;font-family:Arial, Verdana, sans-serif;margin:0px 0px 0px 0px;font-size:1.1em;}
.right-side-effect {background-image:-moz-linear-gradient(center right,#feffff,#4577cb);
background-image:-ms-linear-gradient(right,#4577cb,#3264b6);
background-image:-webkit-gradient(linear,0 0,100% 0,from(#4577cb),to(#feffff));
background-image:-webkit-linear-gradient(right,#feffff,#4577cb);
background-image:-o-linear-gradient(right,#feffff,#4577cb);
background-image:linear-gradient(right,#feffff,#4577cb);
background-repeat:y;}
.div2 {background-color:#ccefe9;border-radius:50px;margin:20px 50px;padding:20px;}
.content-all {background-color:#ffffff;min-width:235px;max-width:1920px;display:block;}
.nav-main {background-color:#3d6fc3;padding:15px 0px 15px 0px;
background-image:-moz-linear-gradient(center top,#4577cb,#3264b6);
background-image:-ms-linear-gradient(top,#4577cb,#3264b6);
background-image:-webkit-gradient(linear,0 0,0 100%,from(#4577cb),to(#3264b6));
background-image:-webkit-linear-gradient(top,#4577cb,#3264b6);
background-image:-o-linear-gradient(top,#4577cb,#3264b6);
background-image:linear-gradient(top,#4577cb,#3264b6);
background-repeat:x;}
.content-main {background-color:#009fe9;padding:10px 0px 10px 0px;text-align:center;}
.right-hand-filler {background-color:#ffffff;width:30px;display:block;}
.logo-main {margin:0px 0px 0px 20px;padding:10px 0px 10px 20px;font-size:200%}
.logo-main a{text-decoration:none;}
.logo-main a:visited{color:#ffffff;}
.logo-main a:visited:hover{color:#bbff11;}
.logo-subtitle {padding:10px 0px 20px 10px;font-size:50%;vertical-align:middle;margin-top:15px;}
.cart {padding: 0 20px 0 0;vertical-align:middle;float:right;}
.header-linkedin{padding 0 0 0 0;margin-right:30px;vertical-align:middle;float:right;background-color:#007fd2;
border-radius: 10px;
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
transition: background 0.5s ease-in-out;}
.header-linkedin:hover{fill:#bbff11;background-color:#22aff4;}
.header-facebook{padding 0 0 0 0;margin-right:10px;vertical-align:middle;float:right;background-color:#007fc9;
border-radius: 10px;
-moz-border-radius: 10px;
-webkit-border-radius: 10px;
transition: background 0.5s ease-in-out;}
.header-facebook:hover{fill:#bbff11;background-color:#22aff4;}
.author-attribution {font-style:normal;font-size:75%;padding-left:10px;float:right;}
.content-fun {background-image:url("images/catch-drone-zoom-1920-2.jpg");height:690px;background-repeat:no-repeat;background-position:left top;}
@media (max-width:1660px) {
 .content-fun {background-image:url("images/catch-drone-zoom-1680-2.jpg");}
}
@media (max-width:1020px) {
 .content-fun {background-image:url("images/catch-drone-zoom-1024.jpg");height:425px;}
}
@media (max-width:550px) {
 .logo-subtitle {display:none;}
 }
@media (max-width:340px) {
 .header-facebook {display:none;}
}
@media (max-width:280px) {
 .logo-main {padding:10px 0 10px 5px;}
 .header-linkedin{margin-right:10px;}
}
@media (max-height:650px) {
 .content-fun{height:425px}
}
.footer {text-align:center;padding:20px 0px 30px 15px;margin-bottom:0px;
background-image:-moz-linear-gradient(center top,#009fe9,#3284d6);
background-image:-ms-linear-gradient(top,#009fe9,#3264b6);
background-image:-webkit-gradient(linear,0 0,0 100%,from(#009fe9),to(#3264b6));
background-image:-webkit-linear-gradient(top,#009fe9,#3264b6);
background-image:-o-linear-gradient(top,#009fe9,#3264b6);
background-image:linear-gradient(top,#009fe9,#3264b6);
background-repeat:x;}
.follow-me {padding-left:25px;}
.copyright {vertical-align:middle;font-size:1em}
.li-btn {vertical-align:middle;}
a:visited {color:#ddff66;
transition:color 0.18s ease;}
a:link {color:#ffffff;
transition:color 0.18s ease;}
a:hover {color:#bbff11;}
a:active {color:#44ff11;}
</style></head>
<body>
 <div class="content-all">
  <div class="nav-main">
   <span class="logo-main"><a href="#">Kris Lion
   <span class="logo-subtitle">"Power to the People!"</span></a></span>
   <!--<span class="logo-subtitle">"Passion: refer to Kristopher Lion."</span>-->
   <!--<span class="logo-subtitle">Your odds of success are proportional to the number of people that want you to succeed</span>-->
   <!--<span class="cart"><a href="http://linkedin.krislion.com"><img src="images/cart.svg" height="50px" width="50px" /><!--<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 51 38.2" enable-background="new 0 0 51 38.2"><path stroke="#fff" stroke-miterlimit="10" d="M48.1 5.3h-7.2l-8 21.7c-.1.3-.3.6-.5.8-.4.5-1.1.8-1.8.8h-21.8c-1.3 0-2.4-1.1-2.4-2.4s1.1-2.4 2.4-2.4h20.2l1.1-2.9h-24.9c-1.3 0-2.4-1.1-2.4-2.4 0-1.3 1.1-2.4 2.4-2.4h26.7l1-2.8h-30c-1.3 0-2.4-1.1-2.4-2.4 0-1.3 1.1-2.4 2.4-2.4h31.8l2.3-6.4c.3-.9 1.2-1.5 2.2-1.6h9c1.3 0 2.4 1.1 2.4 2.4-.1 1.3-1.2 2.4-2.5 2.4zm-34.6 25.5c1.9 0 3.4 1.5 3.4 3.4s-1.5 3.4-3.4 3.4-3.4-1.5-3.4-3.4 1.5-3.4 3.4-3.4zm14.7 0c1.9 0 3.4 1.5 3.4 3.4s-1.5 3.4-3.4 3.4-3.4-1.5-3.4-3.4 1.5-3.4 3.4-3.4z"/></svg></a></span>-->
   <!--<span class="logo-subtitle">"Ship it!"</span>-->
   <!--<span class="author-attribution">-<a href="LINKEDIN.KrisLion.com">W. Brandi</a></span>-->
   <span class="header-linkedin"><a href="http://linkedin.krislion.com"><img height="50px" width="50px" src="images/in.svg" /></a></span>
   <span class="header-facebook"><a href="http://facebook.krislion.com"><img height="50px" width="50px" src="images/f.svg" /></a></span>
  </div>
  <div class="content-fun"><!--<span>Lorem</span><span>Ipsum</span><span>Dolor</span>--></div>
  <div class="content-main">
   <a href="http://12THMAN.KrisLion.com">12thMan</a> |
   <a href="http://BOOK.KrisLion.com">Book</a> |
   <!--<a href="http://BROWNALE.KrisLion.com">Brown Ale</a> |-->
   <a href="http://CANADA.KrisLion.com">Canada</a> |
   <a href="http://CONCEPT.KrisLion.com">Concept</a> |
   <a href="http://DRONES.KrisLion.com">Drones</a> |
   <a href="http://MUSIC.KrisLion.com">Music</a> | 
   <a href="http://PONIES.KrisLion.com">Ponies[@1:14-1:22]</a> |
   <a href="http://ZESTAWIT.KrisLion.com">Zestawit</a>
  <div class="content-main">
   <a href="http://kris-lion.blogspot.com/">Blogspot</a> |
   <a href="http://DEVIANT.KrisLion.com">DeviantArt</a> | 
   <a href="http://FACEBOOK.KrisLion.com">Facebook</a> | 
   <a href="http://GITHUB.KrisLion.com">Github</a> | 
   <a href="http://GOOGLEPLUS.KrisLion.com">GooglePlus</a> | 
   <!--<a href="http://KRISLION.KrisLion.com">Kris Lion</a> | --> 
   <a href="http://LINKEDIN.KrisLion.com">LinkedIn</a> | 
   <a href="http://MYSPACE.KrisLion.com">MySpace</a> | 
   <!--<a href="http://PROFILE.KrisLion.com">Profile</a> |--> 
   <a href="http://STEAM.KrisLion.com">Steam</a> | 
   <a href="http://TWITTER.KrisLion.com">Twitter</a> | 
  </div>
  <div class="content-main">
    may also contact via [my name]@gmail.com --- kris.lion
    <!--<img height="20px" width="300px" src="images/email.svg" />-->
  </div>
  <!--
   <a href="http://DAVERYACK.KrisLion.com">Dave Ryack</a> |
   <a href="http://KAWASAKI.KrisLion.com">Kawasaki</a> | 
   <a href="http://MARA.KrisLion.com">Mara</a> | 
   <a href="http://MULLINS.KrisLion.com">Mullins</a> | 
   <a href="http://NICK.KrisLion.com">Nick</a> | 
   <a href="http://RANDY.KrisLion.com">Randy</a> | 
   <a href="http://TAYLOR.KrisLion.com">Taylor</a> | 
   <a href="http://TOM.KrisLion.com">Tom</a> | 
   <a href="http://YUSUKE.KrisLion.com">Yusuke</a> | 
  -->
  <div class="footer">
   <span class="copyright">
    <a href="http://LINKEDIN.krislion.com" style="text-decoration:none;">&copy; 2000-2014 Kris Lion
     <span class="li-btn">
      <img src="/images/btn_in_20x15.png" width="20" height="15" alt="View Kris Lion's LinkedIn profile" style="vertical-align:middle;margin-bottom:5px" border="0" />
     </span>
    </a>
   </span>
  </div>
  <!--<div class="right-hand-filler">timetimetime&nbsp;</div>-->
 </div>
 <div class="content-main" style="text-align:left">
  (2014-04-20) Coming soon! (eta 4-21, 23, 25 will have updates M-W-F)<br />1. chat on page -or- link to online IRC chat client [mibbit]<br />2. contact form<br />3. twitter button<br />4. steam button<br />5. deviantart button<br />6. all buttons<br />7. more images<br />8. add content to linked sites
 </div>
</body></html>
'''

def home(request):
    return http.HttpResponse(DEFAULT_PAGE) #('Hello Kris Lion!')

