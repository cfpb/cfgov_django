package {"git":
  ensure => "installed"
}
  
package {"java-1.7.0-openjdk":
  ensure => "installed"
}

package {"elasticsearch": 
  ensure => "installed",
  require => YumRepo['elasticsearch']
}

service {"elasticsearch":
  enable => true,
  ensure => "running",
  require => Package['elasticsearch','java-1.7.0-openjdk']
}

service {"firewalld":
  ensure => "stopped",
}
exec { "get-pip.py":
  command => "curl https://bootstrap.pypa.io/get-pip.py >/tmp/get-pip.py && python /tmp/get-pip.py",
  path => "/usr/bin",
  creates => "/usr/bin/pip",
}

 yumrepo { 'elasticsearch':
        descr    => 'elasticsearch repo',
        baseurl  => "http://packages.elastic.co/elasticsearch/1.7/centos",
        gpgcheck => 1,
        gpgkey   => 'http://packages.elastic.co/GPG-KEY-elasticsearch',
        enabled  => 1,
  }

  exec { 'yum Group Install':
      unless  => '/usr/bin/yum grouplist "Development tools" | /bin/grep "^Installed Groups"',
      command => '/usr/bin/yum -y groupinstall "Development tools"',
  }
