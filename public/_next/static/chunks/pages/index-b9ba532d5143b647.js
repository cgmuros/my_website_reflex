(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[405],{5557:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/",function(){return n(8492)}])},8492:function(e,t,n){"use strict";n.r(t),n.d(t,{default:function(){return Component}});var i=n(6811),o=n(7294),r=n(8595),a=n(3100),s=n(4641),l=n(3838),c=n(7754),d=n(1669),h=n(9432),m=n(4418),g=n(9564),x=n(1941),p=n(204),u=n(5034);function useButtonType(e){let[t,n]=(0,o.useState)(!e),i=(0,o.useCallback)(e=>{e&&n("BUTTON"===e.tagName)},[]);return{ref:i,type:t?"button":void 0}}var[f,F]=(0,n(5227).k)({strict:!1,name:"ButtonGroupContext"}),C=n(2504),w=n(5432),Z=n(5893);function ButtonIcon(e){let{children:t,className:n,...i}=e,r=(0,o.isValidElement)(t)?(0,o.cloneElement)(t,{"aria-hidden":!0,focusable:!1}):t,a=(0,w.cx)("chakra-button__icon",n);return(0,Z.jsx)(C.m.span,{display:"inline-flex",alignSelf:"center",flexShrink:0,...i,className:a,children:r})}ButtonIcon.displayName="ButtonIcon";var b=n(295);function ButtonSpinner(e){let{label:t,placement:n,spacing:i="0.5rem",children:r=(0,Z.jsx)(b.$,{color:"currentColor",width:"1em",height:"1em"}),className:a,__css:s,...l}=e,c=(0,w.cx)("chakra-button__spinner",a),d="start"===n?"marginEnd":"marginStart",h=(0,o.useMemo)(()=>({display:"flex",alignItems:"center",position:t?"relative":"absolute",[d]:t?i:0,fontSize:"1em",lineHeight:"normal",...s}),[s,t,d,i]);return(0,Z.jsx)(C.m.div,{className:c,...l,__css:h,children:r})}ButtonSpinner.displayName="ButtonSpinner";var B=n(1103),v=n(5059),_=n(1628),k=n(3179),S=(0,v.G)((e,t)=>{let n=F(),i=(0,_.mq)("Button",{...n,...e}),{isDisabled:r=null==n?void 0:n.isDisabled,isLoading:a,isActive:s,children:l,leftIcon:c,rightIcon:d,loadingText:h,iconSpacing:m="0.5rem",type:g,spinner:x,spinnerPlacement:p="start",className:u,as:f,...b}=(0,k.Lr)(e),v=(0,o.useMemo)(()=>{let e={...null==i?void 0:i._focus,zIndex:1};return{display:"inline-flex",appearance:"none",alignItems:"center",justifyContent:"center",userSelect:"none",position:"relative",whiteSpace:"nowrap",verticalAlign:"middle",outline:"none",...i,...!!n&&{_focus:e}}},[i,n]),{ref:S,type:y}=useButtonType(f),X={rightIcon:d,leftIcon:c,iconSpacing:m,children:l};return(0,Z.jsxs)(C.m.button,{ref:(0,B.qq)(t,S),as:f,type:null!=g?g:y,"data-active":(0,w.PB)(s),"data-loading":(0,w.PB)(a),__css:v,className:(0,w.cx)("chakra-button",u),...b,disabled:r||a,children:[a&&"start"===p&&(0,Z.jsx)(ButtonSpinner,{className:"chakra-button__spinner--start",label:h,placement:"start",spacing:m,children:x}),a?h||(0,Z.jsx)(C.m.span,{opacity:0,children:(0,Z.jsx)(ButtonContent,{...X})}):(0,Z.jsx)(ButtonContent,{...X}),a&&"end"===p&&(0,Z.jsx)(ButtonSpinner,{className:"chakra-button__spinner--end",label:h,placement:"end",spacing:m,children:x})]})});function ButtonContent(e){let{leftIcon:t,rightIcon:n,children:i,iconSpacing:o}=e;return(0,Z.jsxs)(Z.Fragment,{children:[t&&(0,Z.jsx)(ButtonIcon,{marginEnd:o,children:t}),i,n&&(0,Z.jsx)(ButtonIcon,{marginStart:o,children:n})]})}S.displayName="Button";var y=n(1664),X=n.n(y);n(5202);var E=n(9008),z=n.n(E);function Component(){return(0,i.BX)(o.Fragment,{children:[(0,i.tZ)(r.g,{}),(0,i.BX)(a.xu,{children:[(0,i.tZ)(s.U,{sx:{position:"sticky",bg:"#171F26",paddingX:"2em",paddingY:"1em",zIndex:"999",top:"0"},children:(0,i.tZ)(a.xu,{children:(0,i.BX)(s.U,{sx:{fontFamily:"Comfortaa",fontWeight:"500",fontSize:"1.5em"},children:[(0,i.tZ)(l.r,{as:X(),href:"/",sx:{color:"#14A1F0",textDecoration:"none",_hover:{}},children:"cmuros"}),(0,i.tZ)(l.r,{as:X(),href:"/",sx:{color:"#087ec4",textDecoration:"none",_hover:{}},children:"dev"})]})})}),(0,i.tZ)(c.M,{children:(0,i.BX)(d.g,{sx:{maxWidth:"600px",width:"100%",marginY:"2em",padding:"2em"},children:[(0,i.BX)(d.g,{alignItems:"start",spacing:"2em",children:[(0,i.BX)(s.U,{spacing:"1em",children:[(0,i.tZ)(l.r,{as:X(),href:"/",sx:{textDecoration:"none",_hover:{}},children:(0,i.tZ)(h.q,{name:"Cristian Munoz",size:"xl",src:"/me.png",sx:{padding:"2px",color:"#C3C7CB",border:"4px",borderColor:"#14A1F0",bg:"#171F26"}})}),(0,i.BX)(d.g,{alignItems:"start",children:[(0,i.tZ)(m.X,{size:"lg",sx:{color:"#F1F2F4",fontFamily:"Poppins",fontWeight:"500"},children:"Cristian Munoz"}),(0,i.tZ)(g.x,{sx:{marginTop:"0px !important",color:"#C3C7CB"},children:"@cgmuros"}),(0,i.BX)(s.U,{children:[(0,i.tZ)(l.r,{as:X(),href:"https://www.linkedin.com/in/cgmuros/",isExternal:!0,sx:{textDecoration:"none",_hover:{}},children:(0,i.tZ)(x.E,{alt:"Linkedin",src:"/icons/linkedin.svg",sx:{width:"1.5em",height:"1.5em"}})}),(0,i.tZ)(l.r,{as:X(),href:"https://github.com/cgmuros",isExternal:!0,sx:{textDecoration:"none",_hover:{}},children:(0,i.tZ)(x.E,{alt:"Github",src:"/icons/square-github.svg",sx:{width:"1.5em",height:"1.5em"}})}),(0,i.tZ)(l.r,{as:X(),href:"https://twitter.com/cgmurosdev",isExternal:!0,sx:{textDecoration:"none",_hover:{}},children:(0,i.tZ)(x.E,{alt:"Twitter/X",src:"/icons/twitter_logo.svg",sx:{width:"1.5em",height:"1.5em"}})}),(0,i.tZ)(l.r,{as:X(),href:"https://www.strava.com/athletes/49921501",isExternal:!0,sx:{textDecoration:"none",_hover:{}},children:(0,i.tZ)(x.E,{alt:"Strava",src:"/icons/strava_logo.svg",sx:{width:"1.5em",height:"1.5em"}})})]})]})]}),(0,i.BX)(p.k,{sx:{width:"100%"},children:[(0,i.BX)(a.xu,{sx:{fontSize:"0.8em",color:"#C3C7CB"},children:[(0,i.tZ)(g.x,{as:"span",sx:{fontWeight:"bold",color:"#14A1F0"},children:"+15"})," Profesional Experience"]}),(0,i.tZ)(u.L,{}),(0,i.BX)(a.xu,{sx:{fontSize:"0.8em",color:"#C3C7CB"},children:[(0,i.tZ)(g.x,{as:"span",sx:{fontWeight:"bold",color:"#14A1F0"},children:"+10"})," Data Engineer"]}),(0,i.tZ)(u.L,{}),(0,i.BX)(a.xu,{sx:{fontSize:"0.8em",color:"#C3C7CB"},children:[(0,i.tZ)(g.x,{as:"span",sx:{fontWeight:"bold",color:"#14A1F0"},children:"+6"})," Data Architect"]})]}),(0,i.tZ)(g.x,{sx:{color:"#F1F2F4",fontSize:"1.5em"},children:""}),(0,i.BX)(d.g,{alignItems:"start",children:[(0,i.tZ)(g.x,{sx:{color:"#C3C7CB",align:"left"},children:"I have been working for the last 15 years on data-related projects. "}),(0,i.tZ)(g.x,{sx:{color:"#C3C7CB",align:"left"},children:"            Various Companies and Projects have allowed me to gain experience and meet great teams in which I have been able to be a contribution. "}),(0,i.tZ)(g.x,{sx:{color:"#C3C7CB",align:"left"},children:"            I built this site mainly so that you can get to know me and contact me if you need it."})]})]}),(0,i.BX)(d.g,{spacing:"0.8em",sx:{width:"100%"},children:[(0,i.tZ)(m.X,{size:"lg",sx:{width:"100%",size:"lg",paddingTop:"1em",color:"#F1F2F4",fontFamily:"Poppins",fontWeight:"500"},children:"Links"}),(0,i.tZ)(l.r,{as:X(),href:"about",isExternal:!1,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/aboutme.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"About Me"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"A little more about me"})]})]})})}),(0,i.tZ)(l.r,{as:X(),href:"skills",isExternal:!1,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/skills.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"My Skills"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"Knowing my technical skills"})]})]})})}),(0,i.tZ)(l.r,{as:X(),href:"docs/cv_english_detail.pdf",isExternal:!1,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/cv.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"My CV"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"Download my CV"})]})]})})}),(0,i.tZ)(l.r,{as:X(),href:"https://www.linkedin.com/in/cgmuros/",isExternal:!0,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/linkedin.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"LikedIn"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"Let's talk on linkedin"})]})]})})}),(0,i.tZ)(l.r,{as:X(),href:"https://github.com/cgmuros",isExternal:!0,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/square-github.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"Github"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"I invite you to review my repos"})]})]})})}),(0,i.tZ)(l.r,{as:X(),href:"https://twitter.com/cgmurosdev",isExternal:!0,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/twitter_logo.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"Twitter"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"Let's connect"})]})]})})}),(0,i.tZ)(l.r,{as:X(),href:"https://www.strava.com/athletes/49921501",isExternal:!0,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/strava_logo.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"Strava"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"Let's connect"})]})]})})}),(0,i.tZ)(m.X,{size:"lg",sx:{width:"100%",size:"lg",paddingTop:"1em",color:"#F1F2F4",fontFamily:"Poppins",fontWeight:"500"},children:"Contact"}),(0,i.tZ)(l.r,{as:X(),href:"mailto:cgmuros@gmail.com",isExternal:!0,sx:{width:"100%",textDecoration:"none",_hover:{}},children:(0,i.tZ)(S,{sx:{width:"100%",height:"100%",display:"block",padding:"0.5em",borderRadius:"1em",backgroundColor:"#171F26",whiteSpace:"normal",textAlign:"start",color:"#F1F2F4",_hover:{backgroundColor:"#087ec4"}},children:(0,i.BX)(s.U,{sx:{widht:"100%"},children:[(0,i.tZ)(x.E,{src:"icons/envelope-solid.svg",sx:{width:"1.5em",height:"1.5em",margin:"0.8em"}}),(0,i.BX)(d.g,{alignItems:"start",spacing:"0.5em",sx:{paddingY:"0.5em",paddingRight:"0.5em"},children:[(0,i.tZ)(g.x,{sx:{fontFamily:"Poppins",fontWeight:"500",fontSize:"1em",color:"#F1F2F4"},children:"Email"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",fontWeight:"300",color:"#C3C7CB"},children:"cgmuros@gmail.com"})]})]})})})]})]})}),(0,i.BX)(d.g,{sx:{marginBottom:"2em",paddingBottom:"2em",color:"#A3ABB2"},children:[(0,i.tZ)(x.E,{src:"/logo_128.png",sx:{height:"4em"}}),(0,i.tZ)(l.r,{as:X(),href:"https://www.linkedin.com/in/cgmuros/",isExternal:!0,sx:{fontSize:"0.8em",textDecoration:"none",_hover:{}},children:"2023-2024 cgmuros By Cristian Munoz V1"}),(0,i.tZ)(g.x,{sx:{fontSize:"0.8em",marginTop:"0px !important"},children:"Building software from Chile to the World"})]})]}),(0,i.BX)(z(),{children:[(0,i.tZ)("title",{children:"CgmurosDev. Software Engineering and Data"}),(0,i.tZ)("meta",{content:"A Reflex app.",name:"description"}),(0,i.tZ)("meta",{content:"me.png",property:"og:image"})]})]})}},8595:function(e,t,n){"use strict";n.d(t,{g:function(){return Fragment_fd0e7cb8f9fb4669a6805377d925fba0}});var i=n(6811),o=n(7294),r=n(687),a=n(6608),s=n(2752),l=n(1963),c=n(3204),d=n(4504),h=n(3793),m=n(9564);function Fragment_fd0e7cb8f9fb4669a6805377d925fba0(){let[e,t]=(0,o.useContext)(r.DR);return(0,i.tZ)(o.Fragment,{children:(0,a.oA)(null!==t)?(0,i.tZ)(o.Fragment,{children:(0,i.tZ)(s.u_,{isOpen:null!==t,children:(0,i.tZ)(l.Z,{children:(0,i.BX)(c.h,{children:[(0,i.tZ)(d.x,{children:"Connection Error"}),(0,i.tZ)(h.f,{children:(0,i.BX)(m.x,{children:["Cannot connect to server: ",null!==t?t.message:"",". Check if server is reachable at ",(0,a.e9)().href]})})]})})})}):(0,i.tZ)(o.Fragment,{})})}n(5202)}},function(e){e.O(0,[395,202,774,888,179],function(){return e(e.s=5557)}),_N_E=e.O()}]);