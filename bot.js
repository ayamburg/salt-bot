const Discord = require('discord.js');
const client = new Discord.Client();
const auth = require('./auth.json');

let tree = '199698341280481280'

let kevin = '137824628826570752'

let regulars = [
    '151143812272488448', //icesong
    '137824628826570752', //smiles
    '136847796195033090', //myrmidon
    '119955202815164416', //ph3lor
]

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
  }

  if (msg.content === 'list channels') {
    const listedChannels = []; 
    msg.guild.channels.forEach(channel => {
        listedChannels.push(channel);
    });

    console.log(listedChannels);
  }
});

client.on('voiceStateUpdate', (oldMember, newMember) => {
    let oldChannel = oldMember.voiceChannel ? oldMember.voiceChannel.id : null;
    let newChannel = newMember.voiceChannel ? newMember.voiceChannel.id : null;
    if (oldChannel == newChannel || oldChannel != null) return;

    let textChannel = null;

    newMember.guild.channels.forEach(channel => {
        if(channel.position === 0 && channel.type === 'text') {
            textChannel = channel;
        }
    });

    if(newMember.user.id === kevin){
        textChannel.send(`${newMember} you're late again!`);
    }
    else if(regulars.includes(newMember.user.id)) {
        textChannel.send(`${newMember} you're late!`);
    }
});

client.login(auth.token);