
#define MARK 2
#define ONE  1
#define ZERO 0


const int carrier_pin =0;
const int data_pin =1;

// bits for detecting current cycle
volatile bool data_bit =0;
volatile bool carrier_bit =0;
volatile bool process_symbol =0;

volatile unsigned int symbol_frame =0;
volatile unsigned int mil_sec =0;
volatile unsigned int symbol =0;

unsigned int b_cntr = 0;

//varibles used to store sec
unsigned int sec[8];
unsigned int minutes[8];
unsigned int hrs[8];
unsigned int days[8];
unsigned int days2[8];


unsigned int sec_u_d;
unsigned int sec_t_d;
unsigned int min_u_d;
unsigned int min_t_d;
unsigned int hrs_u_d;
unsigned int hrs_t_d;
unsigned int days_u_d;
unsigned int days_t_d;
unsigned int days2_d;

enum reader_states {st_unlock,st_prelock,st_start,st_second,st_minute,st_hour,st_days,st_days2,st_year,st_unused1,st_unused2,st_unused3,st_unused4};
enum reader_states state,next_state;




void setup() {

  Serial.begin(115200);
  // put your setup code here, to run once:
  attachInterrupt(data_pin, int_data,RISING);
  attachInterrupt(carrier_pin, int_carrier,FALLING);

}

void int_data(){
  data_bit = 1;
}

void int_carrier(){

  if(data_bit ==1){
    symbol_frame = symbol_frame << 1;
    symbol_frame = symbol_frame | 0x01;
  }
  else{
    symbol_frame = symbol_frame << 1;
  }

  symbol_frame = symbol_frame & 0x03FF;
  
  if(symbol_frame == 0x03FC){
    symbol = MARK;
  }
  else {
    if(symbol_frame == 0x03E0){
      symbol = ONE;
    }
    else{
      //zero
      symbol = ZERO;
    }
  }

  if(symbol != 0)
  {
    process_symbol =1;
  }
  mil_sec = mil_sec +1;
}


void fsm(){


switch(state){
    case st_unlock:{
      if(symbol==2){
        next_state = st_prelock;
      }
    }
    case st_prelock:{
      if(symbol==2){
        next_state = st_second;
      }
    }

    case st_start:{
      if(symbol==2){
        next_state = st_second;
      }
    }
    case st_second:{
      if(symbol==2){
        next_state = st_minute;
        b_cntr = 0;
      }
      else{
        sec[b_cntr] = symbol;
        b_cntr = b_cntr+1;
      }
      
    }
    case st_minute:{

      if(symbol==2){
        next_state = st_hour;
        b_cntr = 0;
      }
      else{
        minutes[b_cntr] = symbol;
        b_cntr = b_cntr+1;
      }
     
    }

    case st_hour:{

      if(symbol==2){
        next_state = st_days;
        b_cntr = 0;
      }
      else{
        hrs[b_cntr] = symbol;
        b_cntr = b_cntr+1;
      }
     
    }
    case st_days:{

      if(symbol==2){
        next_state = st_days2;
        b_cntr = 0;
      }
      else{
        days[b_cntr] = symbol;
        b_cntr = b_cntr+1;
      }
     
    }

     case st_days2:{

      if(symbol==2){
        next_state =st_year ;
        b_cntr = 0;
      }
      else{
        days2[b_cntr] = symbol;
        b_cntr = b_cntr+1;
      }
     
    }
    case st_year:{

      if(symbol==2){
        next_state =st_unused1 ;
        
      }
      
    }
    case st_unused1:{

      if(symbol==2){
        next_state =st_unused2 ;
      }
      
    }
    case st_unused2:{

      if(symbol==2){
        next_state =st_unused3 ;
      }
      
    }

    case st_unused3:{

      if(symbol==2){
        next_state =st_unused4 ;
      }
      
    }
    case st_unused4:{

      if(symbol==2){
        next_state =st_start ;
        data_integrate();
        serial_print();
      }
      
    }
  
  
  }
  
  //important
  state = next_state;
  
  
}

void data_integrate(){

sec_u_d = sec[0]+sec[1]*2+sec[2]*4+sec[3]*8;
sec_t_d = sec[4]+sec[5]*2+sec[6]*4+sec[7]*8;
min_u_d = minutes[0]+minutes[1]*2+minutes[2]*4+minutes[3]*8;
min_t_d = minutes[4]+minutes[5]*2+minutes[6]*4+minutes[7]*8;
hrs_u_d = hrs[0]+hrs[1]*2+hrs[2]*4+hrs[3]*8;
hrs_t_d = hrs[4]+hrs[5]*2+hrs[6]*4+hrs[3]*8;
days_u_d = days[0]+days[1]*2+days[2]*4+days[3]*8;
days_t_d = days[4]+days[5]*2+days[6]*4+days[7]*8;
days2_d = days2[0]+days2[1]*2+days2[2]*4+days2[3]*8;
  
}

void serial_print(){
  
  Serial.print(days2_d);
  Serial.print(days_t_d);
  Serial.print(days_u_d);
  Serial.print(":");
  Serial.print(hrs_t_d);
  Serial.print(hrs_u_d);
  Serial.print(":");
  Serial.print(min_t_d);
  Serial.print(min_u_d);
  Serial.print(":");
  Serial.print(sec_t_d);
  Serial.println(sec_u_d);
}


void loop() {
  // put your main code here, to run repeatedly:

  if(process_symbol){
     process_symbol =0;
    // call fsm with symbol
    fsm();
    //data integrate
    //data_integrate();
    
  }

}
