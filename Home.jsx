export default function Home() {
return (

<div style={{
background:"#F8F5EE",
minHeight:"100vh",
fontFamily:"Arial",
color:"#222"
}}>

{/* HERO */}

<div style={{
background:
"linear-gradient(135deg,#0B2341,#8B6A2E)",
padding:"70px 20px",
textAlign:"center",
color:"white"
}}>

<h1 style={{
fontSize:"42px",
marginBottom:"10px"
}}>
Our Lady of Dolours
</h1>

<p style={{
fontSize:"18px",
opacity:"0.9"
}}>
Parish Portal • Prayer • Faith • Community
</p>

<div style={{marginTop:"30px"}}>

<button style={{
padding:"14px 26px",
border:"none",
borderRadius:"10px",
background:"#D4AF37",
fontWeight:"bold",
fontSize:"16px",
cursor:"pointer"
}}>
Book Mass Intention
</button>

</div>

</div>


{/* CARDS */}

<div style={{
display:"grid",
gridTemplateColumns:
"repeat(auto-fit,minmax(260px,1fr))",
gap:"20px",
padding:"40px"
}}>

<div style={card}>
<h2>Mass Schedule</h2>
<p>
View daily and Sunday mass timings.
</p>
</div>

<div style={card}>
<h2>Online Booking</h2>
<p>
Book intentions and receive PDF receipts.
</p>
</div>

<div style={card}>
<h2>Prayer Requests</h2>
<p>
Submit intentions and special prayers.
</p>
</div>

</div>


{/* FOOTER */}

<div style={{
background:"#0B2341",
color:"white",
padding:"20px",
textAlign:"center"
}}>
© 2026 Our Lady of Dolours Parish
</div>

</div>

)
}

const card={
background:"white",
padding:"30px",
borderRadius:"18px",
boxShadow:"0 8px 30px rgba(0,0,0,.08)"
}